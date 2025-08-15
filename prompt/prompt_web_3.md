# Landing Page Generator - Premium Glassmorphism + Micro-interactions

## Model

Qwen3-Coder-WebDev  
Token limit: 5,700

## Description

Tạo **landing page HTML chuyên nghiệp** cho sản phẩm hoặc dịch vụ. Giao diện hiện đại, Glassmorphism, micro-interactions, responsive, SEO chuẩn. Output là **1 file HTML chứa cả CSS + JS**, không dùng thư viện ngoài.

## Input Variables

- `[PROJECT_NAME]`: Tên dự án/quán/cửa hàng
- `[APP_PURPOSE]`: Mục đích tạo landing page, tối ưu trải nghiệm và chuyển đổi
- `[PRIMARY_COLOR]`: Màu chính (hex)
- `[ACCENT_COLOR]`: Màu nhấn (hex)
- `[PRODUCT_IMAGE]`: URL ảnh sản phẩm/hero
- `[HERO_TITLE]`: Tiêu đề hero
- `[HERO_SUBTITLE]`: Phụ đề hero
- `[HERO_CTA]`: Text nút hero
- `[MO_TA_QUAN]`: Mô tả quán/cửa hàng/ngắn gọn
- `[MICROCOPY_SUBSCRIBE]`: Text microcopy đăng ký
- `[NAV_ITEMS]`: Danh sách mục navigation
- `[FEATURES]`: Danh sách tính năng, mỗi item gồm `title`, `description`, `icon`
- `[SERVICES]`: Danh sách dịch vụ, mỗi item gồm `title`, `description`, `icon`
- `[GALLERY]`: Danh sách URL ảnh gallery
- `[TESTIMONIALS]`: Danh sách đánh giá, mỗi item gồm `text`, `author`
- `[FAQ]`: Danh sách câu hỏi FAQ, mỗi item gồm `question`, `answer`
- `[CTA_TEXT]`: Text nút CTA cuối trang
- `[CTA_LINK]`: Link nút CTA cuối trang
- `[SEO_TITLE]`: SEO title
- `[SEO_DESCRIPTION]`: SEO description
- `[META_KEYWORDS]`: Meta keywords
- `[MICROCOPY_ORDER_NOTE]`: Microcopy ghi chú order
- `[MICROCOPY_DELIVERY_ESTIMATE]`: Microcopy thời gian giao
- `[MICROCOPY_SECURITY]`: Microcopy thanh toán
- `[BRAND_TONE]`: Tone thương hiệu

## Instructions for AI

1. **Analysis & Planning**

   - Xác định mục tiêu, target audience, tech stack: HTML + CSS + JS trong 1 file.
   - Responsive & fluid layout: desktop, tablet, mobile.
   - Flexible grid cho card: features, services, testimonials.
   - Icons từ [Iconify](https://iconify.design/) theo input.

2. **Frontend Sections**

   - Header: logo, nav items, fixed, Glassmorphism.
   - Hero: image, title, subtitle, CTA button.
   - Features: Glassmorphism cards, hover effect, icon.
   - Services: Glassmorphism cards, hover effect, icon.
   - Gallery: responsive grid, hover animation.
   - Testimonials: slider, Glassmorphism cards, smooth transition.
   - FAQ: accordion micro-interactions.
   - CTA section: button with hover effect.
   - Footer: contact info, copyright, back-to-top button.

3. **Micro-interactions & Animations**

   - Hover card lift + shadow.
   - Smooth scroll for nav anchor.
   - Slider testimonial tự động và có nút next/prev.
   - Accordion FAQ: toggle question/answer.
   - Back-to-top button: fade-in/fade-out + smooth scroll.

4. **Deployment Considerations**
   - Output 1 file HTML duy nhất.
   - Color theme áp dụng đồng nhất.
   - Placeholder images từ `[PRODUCT_IMAGE]` hoặc demo ảnh.
   - SEO tags + meta keywords + microcopy đầy đủ.

## Example Input (giá trị thực cho các biến trên)

```text
[PROJECT_NAME]: Cà Phê Sáng Tạo
[APP_PURPOSE]: Tạo landing page quán cà phê hiện đại, Glassmorphism + Micro-interactions, tối ưu trải nghiệm và chuyển đổi khách hàng
[PRIMARY_COLOR]: #6F4E37
[ACCENT_COLOR]: #F2C57C
[PRODUCT_IMAGE]: https://picsum.photos/1200/600?random=11
[HERO_TITLE]: Hương Vị Tinh Tế — Khơi Nguồn Sáng Tạo
[HERO_SUBTITLE]: Thưởng thức cà phê chọn lọc, pha tay thủ công trong không gian Glassmorphism đầy cảm hứng
[HERO_CTA]: Đặt Bàn & Ưu Đãi Ngay
[MO_TA_QUAN]: Trải nghiệm cà phê tinh túy — hạt chọn lọc, barista tay nghề cao, không gian ấm cúng và sáng tạo
[MICROCOPY_SUBSCRIBE]: Đăng ký để nhận ưu đãi độc quyền — giảm 15% lần đầu
[NAV_ITEMS]: Trang chủ, Menu, Dịch vụ, Bộ sưu tập, Đánh giá, FAQ, Liên hệ
[FEATURES]:
- title: Hạt cà phê chọn lọc
  description: Rang theo công thức giữ trọn hương vị
  icon: mdi:coffee
- title: Barista chuyên nghiệp
  description: Pha chế thủ công, sáng tạo thức uống
  icon: mdi:barista
- title: Cold brew & Signature blends
  description: Trải nghiệm vị cà phê mới lạ
  icon: mdi:cup
- title: Không gian thư giãn & làm việc
  description: Wifi tốc độ cao, ổ cắm tiện lợi, ánh sáng dịu nhẹ
  icon: mdi:sofa
[SERVICES]:
- title: Giao hàng nhanh
  description: Trong 60–90 phút nội thành
  icon: mdi:truck-fast
- title: Đặt trước & ưu tiên nhóm
  description: Phục vụ cho nhóm/meeting qua form nhanh
  icon: mdi:calendar-check
[GALLERY]:
- https://picsum.photos/400/300?gallery=21
- https://picsum.photos/400/300?gallery=22
- https://picsum.photos/400/300?gallery=23
- https://picsum.photos/400/300?gallery=24
[TESTIMONIALS]:
- text: "Cà phê đậm đà, barista thân thiện — mình đến mỗi tuần!"
  author: Minh K.
- text: "Không gian sáng tạo, làm việc cả ngày vẫn thoải mái."
  author: Linh A.
[FAQ]:
- question: Quán mở cửa giờ nào?
  answer: Mở cửa hàng ngày từ 07:00 đến 22:00, cuối tuần có chương trình âm nhạc nhẹ từ 18:00
- question: Có nhận đặt tiệc nhỏ hoặc họp nhóm không?
  answer: Có — đặt trước qua form hoặc hotline
[CTA_TEXT]: Đặt Bàn Ngay — Nhận Ưu Đãi
[CTA_LINK]: #booking
[SEO_TITLE]: Cà Phê Sáng Tạo — Quán Cà Phê Thủ Công, Không Gian Sáng Tạo & Giao Hàng Nhanh
[SEO_DESCRIPTION]: Cà Phê Sáng Tạo — hạt cà phê chọn lọc, barista chuyên nghiệp, không gian lý tưởng. Đặt bàn ngay để nhận ưu đãi 15%
[META_KEYWORDS]: cà phê thủ công, quán cà phê, cold brew, barista, đặt bàn, giao hàng
[MICROCOPY_ORDER_NOTE]: Chọn kích cỡ, ghi chú pha chế và thời gian nhận — xác nhận đơn trong 10 phút
[MICROCOPY_DELIVERY_ESTIMATE]: Thời gian giao dự kiến: 60–90 phút
[MICROCOPY_SECURITY]: Thanh toán an toàn — hỗ trợ thẻ, ví điện tử, thanh toán khi nhận hàng
[BRAND_TONE]: Ấm áp, tinh tế, sáng tạo — thân thiện nhưng chuyên nghiệp
```

## Example Output

<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[PROJECT_NAME]</title>
  <meta name="description" content="[SEO_DESCRIPTION]">
  <meta name="keywords" content="[META_KEYWORDS]">
  <style>
    /* CSS Glassmorphism + layout + animations */
    body { font-family: sans-serif; margin: 0; padding: 0; background: linear-gradient(135deg, #f0f0f0, #e0e0e0); }
    header, section, footer { padding: 2rem; }
    .glass-card { backdrop-filter: blur(10px); background: rgba(255,255,255,0.2); border-radius: 1rem; padding: 1rem; margin: 1rem 0; }
    button { background-color: [ACCENT_COLOR]; border: none; color: white; padding: 0.75rem 1.5rem; border-radius: 0.5rem; cursor: pointer; transition: transform 0.2s; }
    button:hover { transform: scale(1.05); }
  </style>
</head>
<body>
  <header>
    <nav>
      [NAV_ITEMS]
    </nav>
  </header>
  <section class="hero">
    <img src="[PRODUCT_IMAGE]" alt="[PROJECT_NAME]">
    <h1>[HERO_TITLE]</h1>
    <p>[HERO_SUBTITLE]</p>
    <button>[HERO_CTA]</button>
  </section>
  <section class="features">
    [FEATURES]
  </section>
  <section class="services">
    [SERVICES]
  </section>
  <section class="gallery">
    [GALLERY]
  </section>
  <section class="testimonials">
    [TESTIMONIALS]
  </section>
  <section class="faq">
    [FAQ]
  </section>
  <section class="cta">
    <button onclick="location.href='[CTA_LINK]'">[CTA_TEXT]</button>
  </section>
  <footer>
    <p>[MICROCOPY_SECURITY]</p>
  </footer>
  <script>
    // JS cho slider, accordion FAQ, smooth scroll, back-to-top
  </script>
</body>
</html>
