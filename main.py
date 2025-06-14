import streamlit as st
import random
import time

st.set_page_config(page_title="🎯 Vòng Quay May Mắn", layout="centered")

st.title("🎯 VÒNG QUAY MAY MẮN")
st.write("Nhập danh sách người chơi hoặc phần thưởng để quay ngẫu nhiên.")

# Nhập danh sách
items = st.text_area("📝 Nhập mỗi dòng là một người/chọn:", placeholder="Phần thưởng 1\nPhần thưởng 2\nPhần thưởng 3").split('\n')
items = [item.strip() for item in items if item.strip() != '']

if len(items) < 2:
    st.warning("🔔 Vui lòng nhập ít nhất 2 mục để quay.")
    st.stop()

# Nút quay
if st.button("🎉 QUAY NGAY"):
    with st.spinner("🔄 Đang quay..."):
        spin_time = 3  # Giả lập thời gian quay
        for i in range(spin_time * 10):
            chosen = random.choice(items)
            st.write(f"👉 {chosen}")
            time.sleep(0.1)
            st.experimental_rerun()  # Tái chạy để làm hiệu ứng quay

    winner = random.choice(items)
    st.success(f"🎉 KẾT QUẢ: **{winner}** 🎊")
