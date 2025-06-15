import streamlit as st
import random
import plotly.graph_objects as go

# Cấu hình trang
st.set_page_config(page_title="🎯 Vòng quay may mắn có xác suất", layout="centered")
st.title("🎯 VÒNG QUAY MAY MẮN")
st.markdown("Nhập các phần thưởng và xác suất tương ứng để quay vòng.")

# Giao diện nhập liệu
with st.form("form_inputs"):
    names_input = st.text_area("🎁 Danh sách phần thưởng/người chơi (mỗi dòng 1 mục):", "A\nB\nC\nD")
    weights_input = st.text_area("📊 Tỷ lệ phần trăm tương ứng (theo dòng):", "25\n25\n25\n25")
    submitted = st.form_submit_button("✅ Cập nhật vòng quay")

# Xử lý dữ liệu
names = [n.strip() for n in names_input.split('\n') if n.strip()]
weights = [float(w.strip()) for w in weights_input.split('\n') if w.strip()]

if len(names) != len(weights):
    st.error("❌ Số lượng mục và số lượng tỷ lệ không khớp!")
    st.stop()

if sum(weights) != 100:
    st.warning("⚠️ Tổng xác suất không bằng 100%. Sẽ tự động chuẩn hóa.")
    total_weight = sum(weights)
    weights = [w * 100 / total_weight for w in weights]

# Vẽ biểu đồ vòng quay
fig = go.Figure(data=[go.Pie(
    labels=names,
    values=weights,
    hole=0.3,
    textinfo='label+percent',
    marker=dict(line=dict(color='#000000', width=1))
)])
fig.update_layout(showlegend=False)

st.plotly_chart(fig, use_container_width=True)

# Nút quay
if st.button("🎉 QUAY NGAY"):
    result = random.choices(names, weights=weights, k=1)[0]
    st.success(f"🎯 KẾT QUẢ: **{result}** 🎊")
