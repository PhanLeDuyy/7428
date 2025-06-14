import streamlit as st
import random

st.title("🎲 Trò chơi Tài Xỉu - Phiên bản xúc xắc 🎲")

st.write("Chọn Tài hoặc Xỉu, sau đó bấm nút để tung 3 viên xúc xắc.")

# Người chơi chọn Tài hay Xỉu
choice = st.radio("Bạn chọn:", ("Tài", "Xỉu"))

# Hàm chuyển số xúc xắc sang emoji tương ứng
def dice_emoji(value):
    dice_emojis = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅",
    }
    return dice_emojis.get(value, "")

if st.button("Tung xúc xắc!"):
    dice = [random.randint(1, 6) for _ in range(3)]
    total = sum(dice)

    # Hiển thị xúc xắc dưới dạng emoji
    dice_display = "  ".join(dice_emoji(d) for d in dice)
    st.markdown(f"**3 viên xúc xắc:** {dice_display}")
    st.markdown(f"**Tổng điểm:** {total}")

    result = "Tài" if total >= 11 else "Xỉu"
    st.markdown(f"**Kết quả:** {result}")

    if choice == result:
        st.success("🎉 Bạn đã thắng! 🎉")
    else:
        st.error("😢 Bạn đã thua! 😢")
