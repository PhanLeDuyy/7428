import streamlit as st
import qrcode
from io import BytesIO

# Nhập link
fb_link = st.text_input("🔗 Nhập link bài viết Facebook:", placeholder="https://facebook.com/abc...")

if st.button("🎯 Tạo QR Code") and fb_link:
    # Tạo QR Code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(fb_link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')  # Đảm bảo ảnh RGB

    # Hiển thị ảnh
    st.image(img, caption="📷 Mã QR để chia sẻ", use_column_width=False)

    # ✅ Chuyển ảnh thành bytes để tải về
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Nút tải ảnh
    st.download_button(
        label="⬇️ Tải mã QR",
        data=byte_im,
        file_name="fb_qrcode.png",
        mime="image/png"
    )
