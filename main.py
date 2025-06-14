import streamlit as st
import random

st.set_page_config(page_title="Tài Xỉu Game", layout="wide")

# Custom CSS để tạo phong cách giống hình
st.markdown("""
<style>
/* Toàn bộ body nền tối */
body {
    background-color: #121212;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Khung chính */
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 30px;
    margin-top: 50px;
}

/* Vùng Tài và Xỉu */
.card {
    width: 300px;
    height: 220px;
    border-radius: 15px;
    padding: 20px;
    position: relative;
    box-shadow: 0 0 15px rgba(0,0,0,0.6);
}

/* Tài màu xanh lá */
.tai {
    background: linear-gradient(135deg, #1de9b6, #00bfa5);
    box-shadow: 0 0 20px #00bfa5;
}

/* Xỉu màu hồng */
.xiu {
    background: linear-gradient(135deg, #ff6e7f, #bfe9ff);
    box-shadow: 0 0 20px #ff6e7f;
}

/* Tiêu đề Tài, Xỉu to */
.title {
    font-size: 4rem;
    font-weight: 900;
    user-select: none;
}

/* Số tiền cược */
.bet-amount {
    margin-top: 10px;
    font-size: 1.3rem;
    font-weight: bold;
    color: gold;
}

/* Nút cược */
.bet-button {
    margin-top: 20px;
    width: 100%;
    padding: 12px;
    font-weight: 700;
    font-size: 1.2rem;
    border-radius: 10px;
    cursor: pointer;
    background-color: gold;
    color: black;
    border: none;
    transition: 0.3s ease;
}

.bet-button:hover {
    background-color: #ffaa00;
}

/* Vòng tròn trung tâm */
.center-circle {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    background: radial-gradient(circle, #222222 60%, #ffb300 100%);
    box-shadow: 0 0 30px #ffb300;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2.2rem;
    font-weight: 900;
    color: white;
    user-select: none;
    flex-wrap: wrap;
    text-align: center;
    padding: 10px;
}

/* Thanh trạng thái */
.status-bar {
    margin-top: 40px;
    width: 90%;
    height: 20px;
    background: #333;
    border-radius: 10px;
    display: flex;
    gap: 5px;
    padding: 5px;
    justify-content: center;
    align-items: center;
    user-select: none;
}

.status-dot {
    width: 18px;
    height: 18px;
    border-radius: 50%;
}

.status-tai {
    background-color: #00bfa5;
    box-shadow: 0 0 6px #00bfa5;
}

.status-xiu {
    background-color: #ff6e7f;
    box-shadow: 0 0 6px #ff6e7f;
}
</style>
""", unsafe_allow_html=True)

# Khởi tạo biến trong session_state
if 'bet_tai' not in st.session_state:
    st.session_state.bet_tai = 0
if 'bet_xiu' not in st.session_state:
    st.session_state.bet_xiu = 0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'last_dice' not in st.session_state:
    st.session_state.last_dice = None
if 'last_result' not in st.session_state:
    st.session_state.last_result = None

# Layout 3 cột
col1, col2, col3 = st.columns([3, 1, 3])

with col1:
    st.markdown('<div class="card tai">', unsafe_allow_html=True)
    st.markdown('<div class="title">TÀI</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="bet-amount">Cược: {st.session_state.bet_tai:,}</div>', unsafe_allow_html=True)
    if st.button("Cược TÀI"):
        st.session_state.bet_tai += 1000
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    center_value = st.empty()
    # Hiển thị xúc xắc và tổng nếu đã chơi
    dice = st.session_state.last_dice
    if dice:
        total = sum(dice)
        dice_str = " + ".join(str(d) for d in dice)
        center_value.markdown(f'<div class="center-circle">{dice_str} = {total}</div>', unsafe_allow_html=True)
    else:
        center_value.markdown(f'<div class="center-circle">...</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card xiu">', unsafe_allow_html=True)
    st.markdown('<div class="title">XỈU</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="bet-amount">Cược: {st.session_state.bet_xiu:,}</div>', unsafe_allow_html=True)
    if st.button("Cược XỈU"):
        st.session_state.bet_xiu += 1000
    st.markdown('</div>', unsafe_allow_html=True)

# Thanh trạng thái lịch sử tài/xỉu
st.markdown('<div class="status-bar">', unsafe_allow_html=True)
for result in st.session_state.history[-20:]:
    if result == "TÀI":
        st.markdown('<div class="status-dot status-tai"></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-dot status-xiu"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Nút chơi tung xúc xắc
if st.button("Chơi ngay!"):
    dice = [random.randint(1,6) for _ in range(3)]
    total = sum(dice)
    ket_qua = "TÀI" if total >= 11 else "XỈU"
    # Lưu trạng thái
    st.session_state.last_dice = dice
    st.session_state.last_result = ket_qua
    st.session_state.history.append(ket_qua)
    st.experimental_rerun()

# Hiển thị kết quả thắng thua
if st.session_state.last_result:
    st.markdown(f"### Kết quả: **{st.session_state.last_result}** thắng!")
