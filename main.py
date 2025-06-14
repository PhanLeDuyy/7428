# Xóa dòng tạo số ngẫu nhiên bên ngoài nút chơi (number = random.randint(4,17))
# Thay bằng biến trống hiển thị kết quả xúc xắc
center_value = st.empty()

# Khi nhấn nút "Chơi ngay!"
if st.button("Chơi ngay!"):
    # Tung 3 xúc xắc
    dice = [random.randint(1,6) for _ in range(3)]
    total = sum(dice)
    # Hiển thị xúc xắc
    center_value.markdown(f'<div class="center-circle">{" + ".join(map(str,dice))} = {total}</div>', unsafe_allow_html=True)
    # Xác định kết quả TÀI hay XỈU
    ket_qua = "TÀI" if total >= 11 else "XỈU"
    st.write(f"**Kết quả: {ket_qua} thắng!**")
    # Lưu lịch sử
    st.session_state.history.append(ket_qua)
    # Reload lại trang để cập nhật
    st.experimental_rerun()
else:
    # Khi chưa bấm, hiển thị mặc định trống hoặc hướng dẫn
    center_value.markdown(f'<div class="center-circle">...</div>', unsafe_allow_html=True)
