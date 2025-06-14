import streamlit as st
import random

st.title("Trò chơi Tài Xỉu")

# Người chơi chọn Tài hay Xỉu
choice = st.radio("Bạn chọn:", ("Tài", "Xỉu"))

if st.button("Quăng xúc xắc!"):
    dice = [random.randint(1, 6) for _ in range(3)]
    total = sum(dice)

    st.write(f"3 viên xúc xắc: {dice}")
    st.write(f"Tổng điểm: {total}")

    result = "Tài" if total >= 11 else "Xỉu"
    st.write(f"Kết quả: {result}")

    if choice == result:
        st.success("Bạn đã thắng! 🎉")
    else:
        st.error("Bạn đã thua! 😢")
