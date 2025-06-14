import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="Tạo QR Code chia sẻ bài viết Facebook", page_icon="📱", layout="centered")

st.title("📱 Tạo QR Code để chia sẻ bài viết Facebook")
st.write("Nhập liên kết bài viết Facebook để tạo mã QR có thể quét được.")

# Nhập link Facebook
fb_link = st.text_input("🔗 Nhập link bài viết Facebook:", placeholder="https://www.facebook.com/yourpostlink")

# Tạo QR khi nhấn nút
if st.button("🎯 Tạo QR Code") and fb_link:
    try:
        # Tạo QR code
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )
        qr.add_data(fb_link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Hiển thị ảnh
        st.image(img, caption="📷 Mã QR để chia sẻ", use_column_width=False)

        # Cho tải xuống
        buf = BytesIO()
        img.save(buf)
        byte_im = buf.getvalue()

        st.download_button(
            label="⬇️ Tải mã QR",
            data=byte_im,
            file_name="fb_qrcode.png",
            mime="image/png"
        )
    except Exception as e:
        st.error(f"❌ Lỗi: {e}")
elif not fb_link:
    st.info("💡 Hãy nhập link bài viết trước khi tạo mã QR.")
