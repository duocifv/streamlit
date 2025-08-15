# Prompt: Tạo Landing Page Hoàn Chỉnh theo Material Design 3 (1 file HTML/CSS/JS)

Bạn là **lập trình viên web chuyên nghiệp** và **UI/UX designer xuất sắc**.  
Nhiệm vụ: **tạo một landing page hoàn chỉnh trong 1 file HTML**, có HTML, CSS và JS, **tham khảo**, dựa trên dữ liệu sản phẩm/doanh nghiệp mà tôi cung cấp.  
**Tất cả thiết kế, màu sắc, shadow, animation, hiệu ứng hover, layout** phải theo **Material Design 3 (M3)**: https://m3.material.io/

---

## Dữ liệu đầu vào

- Tên sản phẩm/doanh nghiệp: {ten_san_pham}
- Mô tả sản phẩm: {mo_ta_san_pham}
- Hình ảnh hero: {url_hero} (ví dụ: https://picsum.photos/800/400)
- Màu chủ đạo: {mau_chu_dao} (ví dụ: #6200EE)
- Tính năng 1: {tinh_nang_1}
- Tính năng 2: {tinh_nang_2}
- Tính năng 3: {tinh_nang_3}
- Dịch vụ 1..3: {dich_vu_1}..{dich_vu_3}
- Gallery hình ảnh 1..4: {gallery_1}..{gallery_4} (ví dụ: https://picsum.photos/300/200?random=1..4)
- Testimonial 1..3: {ten_khach_1}, {noi_dung_1} …
- FAQ 1..3: {cau_hoi_1}, {tra_loi_1} …
- CTA: {cta_text}, {cta_link}

---

## Yêu cầu output

1. **Tất cả HTML + CSS + JS trong 1 file**, không tách file ngoài.
2. **Responsive** cho desktop và mobile.
3. Layout đầy đủ:
   - Header: logo/tên sản phẩm + menu (Home, Features, Services, Gallery, FAQ, Contact)
   - Hero: hình ảnh + mô tả ngắn + nút CTA
   - Features: 3 tính năng nổi bật
   - Services: 3 dịch vụ chính
   - Gallery: 4 hình sản phẩm
   - Testimonials: 3 feedback
   - FAQ: 3 câu hỏi & trả lời
   - Footer: thông tin bản quyền + liên hệ
   - Scroll-to-top button
4. **Material Design 3 (M3)**:
   - Shadow, elevation cho các section và card
   - Nút theo M3: màu chủ đạo, hover, ripple effect
   - Typography: font M3 (Roboto/Google Fonts), tiêu đề và nội dung theo style M3
   - Animation nhẹ: fade, slide, hover, transitions
   - Responsive layout theo M3 guidelines
5. Màu sắc **chủ đạo**: {mau_chu_dao}, áp dụng thống nhất toàn trang.
6. Chỉ xuất **HTML + CSS + JS**, không giải thích thêm, không bình luận.

---

## Ví dụ dữ liệu mẫu

- Tên sản phẩm: Cà Phê Sáng Tạo
- Mô tả: Trải nghiệm cà phê tinh túy với hương vị độc đáo, nguyên liệu sạch, cách pha chuyên nghiệp.
- Hero image: https://picsum.photos/800/400
- Màu chủ đạo: #6F4E37
- Tính năng: Nguyên liệu 100% hạt cà phê chọn lọc; Pha chế bởi barista chuyên nghiệp; Giao hàng nhanh, tận nơi
- Services: Tư vấn pha chế, Workshop cà phê, Đặt hàng online
- Gallery: https://picsum.photos/300/200?random=1..4
- Testimonial: Nam - Khách hàng: “Cà phê tuyệt vời, dịch vụ chu đáo” …
- FAQ: “Cà phê có bảo quản lâu không?” → “Có, trong 1 tuần ở nhiệt độ phòng” …
- CTA: Mua Ngay → /order
