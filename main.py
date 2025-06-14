import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Ủng hộ trẻ em châu Phi", layout="centered")

# --- CSS đơn giản cho phong cách cảm động ---
st.markdown("""
    <style>
    .big-title {
        font-size: 3rem;
        font-weight: 800;
        color: #ff6347;
        text-align: center;
    }
    .subtext {
        font-size: 1.2rem;
        text-align: center;
        margin-top: -10px;
        color: #555;
    }
    .thank-you {
        font-size: 1.1rem;
        color: green;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Tiêu đề chính ---
st.markdown('<div class="big-title">Ủng hộ Trẻ Em Châu Phi</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Mỗi đóng góp của bạn là một tia hy vọng cho các em nhỏ đang đói khát và thiếu thốn</div>', unsafe_allow_html=True)

# --- Hình ảnh minh họa ---
st.image("https://i.imgur.com/5oCz4KC.jpg", use_column_width=True, caption="Nguồn: UNICEF")

# --- Form ủng hộ ---
st.header("🤝 Gửi tấm lòng của bạn")

with st.form("donate_form"):
    name = st.text_input("Tên của bạn", max_chars=30)
    amount = st.selectbox("Số tiền muốn ủng hộ", [50000, 100000, 200000, 500000, 1000000], format_func=lambda x: f"{x:,} VNĐ")
    message = st.text_area("Lời nhắn gửi đến các em nhỏ", max_chars=200)
    submit = st.form_submit_button("Gửi ủng hộ")

    if submit and name:
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        # Lưu tạm vào session_state
        if 'donors' not in st.session_state:
            st.session_state.donors = []
        st.session_state.donors.append({
            "name": name,
            "amount": amount,
            "message": message,
            "time": now
        })
        st.success("❤️ Cảm ơn bạn đã ủng hộ!")

# --- Hiển thị danh sách người đã ủng hộ ---
if 'donors' in st.session_state and st.session_state.donors:
    st.header("📜 Danh sách ủng hộ")
    for donor in reversed(st.session_state.donors[-10:]):  # Hiện 10 người gần nhất
        st.markdown(f"""
        **🧍 {donor['name']}** - ủng hộ **{donor['amount']:,} VNĐ** *(vào {donor['time']})*  
        > _"{donor['message']}"_
        ---
        """)

# --- Footer ---
st.markdown("---")
st.markdown("*Dự án thiện nguyện phi lợi nhuận. Mọi số tiền thu được sẽ gửi trực tiếp qua tổ chức từ thiện quốc tế.*")
