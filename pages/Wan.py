import streamlit as st
from PIL import Image
import tempfile
import time
import io

# Kiểm tra gradio_client
try:
    from gradio_client import Client
except ImportError:
    st.error("⚠️ Thiếu module gradio_client. Chạy: pip install gradio-client")
    st.stop()

# Cấu hình Streamlit
st.set_page_config(
    page_title="🎬 Image to Video Generator",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Image to Video Generator - Wan2.2 I2V")

# Upload ảnh
uploaded_file = st.file_uploader(
    "📤 Chọn ảnh (PNG/JPG, tối đa 10MB)",
    type=["png", "jpg", "jpeg"]
)

# Prompt
prompt = st.text_area(
    "✍️ Mô tả video (tiếng Anh)",
    value="A cheerful woman dancing in a playful way",
    height=80
)

# Resize và chuẩn bị ảnh bytes
def prepare_image_bytes(file):
    image = Image.open(file)
    max_size = (512, 512)
    if image.size[0] > max_size[0] or image.size[1] > max_size[1]:
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
    # Lưu ảnh vào bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    return img_byte_arr, image

# Nút Generate
if st.button("🎬 Generate Video"):

    if not uploaded_file or not prompt.strip():
        st.warning("⚠️ Vui lòng upload ảnh và nhập prompt")
    else:
        progress_bar = st.progress(0)
        status_text = st.empty()

        try:
            # Chuẩn bị ảnh
            status_text.text("🔄 Chuẩn bị ảnh...")
            img_bytes, image = prepare_image_bytes(uploaded_file)
            progress_bar.progress(20)
            st.image(image, caption="Ảnh đã chuẩn bị", use_column_width=True)

            # Kết nối Gradio Space
            status_text.text("🌐 Kết nối Gradio Space...")
            if 'client' not in st.session_state:
                st.session_state.client = Client(
                    "https://zerogpu-aoti-wan2-2-fp8da-aoti-faster.hf.space"
                )
            client = st.session_state.client
            progress_bar.progress(50)

            # Gọi API tạo video
            status_text.text("🎬 Đang tạo video (có thể mất vài phút)...")
            result = None
            for i in range(3):  # Retry 3 lần nếu fail
                try:
                    # Sử dụng dict input, ảnh bytes
                    result = client.predict(
                        {
                            "prompt": prompt,
                            "image": img_bytes
                        },
                        fn_index=0
                    )
                    break
                except Exception as e:
                    time.sleep(2)

            progress_bar.progress(90)

            if result:
                status_text.text("✅ Hoàn thành!")
                st.success("🎉 Video đã được tạo!")
                st.video(result)
            else:
                st.error("❌ Không nhận được kết quả từ model. Thử lại sau hoặc giảm kích thước ảnh (<512x512).")

        except Exception as e:
            st.error(f"❌ Lỗi: {str(e)}")

        finally:
            # Dọn file tạm nếu có
            try:
                import os
                if 'temp_image_path' in locals():
                    os.unlink(temp_image_path)
            except:
                pass
            time.sleep(2)
            progress_bar.empty()
            status_text.empty()
