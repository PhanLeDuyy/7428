col2 = st.columns([1])[0]

center_value = st.empty()
number = random.randint(4,17)
center_value.markdown(f'<div class="center-circle">{number}</div>', unsafe_allow_html=True)

# Nút chơi
if st.button("Chơi ngay!"):
    ket_qua = "TÀI" if number >= 11 else "XỈU"
    st.session_state.history.append(ket_qua)
    st.experimental_rerun()
