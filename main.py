import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(page_title="🎯 Vòng quay may mắn có xác suất", layout="centered")
st.title("🎯 Vòng quay may mắn có xác suất")

st.markdown("""
Nhập từng phần thưởng mỗi dòng, và tỷ lệ phần trăm tương ứng cách nhau dấu phẩy.<br>
Ví dụ phần thưởng:<br>
<pre>
Thưởng Gia Linh
Thưởng Lê Duy    
Thưởng 16prm
</pre>
Tỷ lệ phần trăm:<br>
<pre>
50,50,0
</pre>
Tổng tỷ lệ nên bằng 100.
""", unsafe_allow_html=True)

# Nhập phần thưởng
prizes_text = st.text_area("Phần thưởng (mỗi dòng 1 phần thưởng)", "A\nB\nC\nD")
weights_text = st.text_input("Tỷ lệ phần trăm tương ứng (cách nhau dấu phẩy)", "50,20,20,10")

prizes = [p.strip() for p in prizes_text.strip().split("\n") if p.strip()]
weights_strs = [w.strip() for w in weights_text.strip().split(",") if w.strip()]

if len(prizes) != len(weights_strs):
    st.error("❌ Số phần thưởng và số tỷ lệ phải bằng nhau!")
    st.stop()

try:
    weights = [float(w) for w in weights_strs]
except:
    st.error("❌ Tỷ lệ phần trăm phải là các số hợp lệ!")
    st.stop()

total = sum(weights)
if total <= 0:
    st.error("❌ Tổng tỷ lệ phải lớn hơn 0!")
    st.stop()

# Chuẩn hóa tỷ lệ thành phần trăm
weights = [w / total * 100 for w in weights]

wheel_code = f"""
<style>
  body {{
    font-family: sans-serif;
    text-align: center;
    background: #f3f3f3;
    margin: 0; padding: 0;
  }}
  #wheel {{
    margin: 40px auto;
    width: 400px;
    height: 400px;
    border-radius: 50%;
    border: 10px solid #333;
    position: relative;
    overflow: hidden;
    box-shadow: 0 0 20px rgba(0,0,0,0.2);
    transform: rotate(0deg);
  }}
  .segment {{
    width: 50%;
    height: 200px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform-origin: 0% 0%;
    clip-path: polygon(0 0, 100% 0, 0 100%);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: bold;
  }}
  #spin {{
    margin-top: 20px;
    padding: 10px 20px;
    font-size: 20px;
    cursor: pointer;
  }}
  #pointer {{
    width: 0;
    height: 0;
    border-left: 20px solid transparent;
    border-right: 20px solid transparent;
    border-bottom: 30px solid red;
    position: absolute;
    top: -30px;
    left: calc(50% - 20px);
  }}
</style>

<h1>🎯 Vòng Quay May Mắn</h1>
<div id="wheel">
  <div id="pointer"></div>
</div>
<button id="spin">QUAY</button>

<script>
  const items = {json.dumps(prizes)};
  const weights = {json.dumps(weights)};
  const colors = ["#f44336", "#4caf50", "#2196f3", "#ff9800", "#9c27b0", "#ff5722", "#795548", "#607d8b"];
  const wheel = document.getElementById("wheel");

  wheel.querySelectorAll(".segment").forEach(el => el.remove());

  function drawWheel() {{
    for (let i = 0; i < items.length; i++) {{
      const segment = document.createElement("div");
      segment.className = "segment";
      segment.style.background = colors[i % colors.length];
      const angle = i * (360 / items.length);
      segment.style.transform = `rotate(${angle}deg)`;
      segment.innerHTML = items[i];
      wheel.appendChild(segment);
    }}
  }}

  function weightedChoice(items, weights) {{
    const total = weights.reduce((a, b) => a + b, 0);
    const r = Math.random() * total;
    let sum = 0;
    for (let i = 0; i < items.length; i++) {{
      sum += weights[i];
      if (r < sum) return i;
    }}
    return 0;
  }}

  function spinWheel() {{
    const selectedIndex = weightedChoice(items, weights);
    const anglePerItem = 360 / items.length;
    const baseAngle = selectedIndex * anglePerItem;
    const extra = 360 * 5; // quay 5 vòng
    const finalAngle = extra + (360 - baseAngle - anglePerItem / 2);

    wheel.style.transition = "transform 5s ease-out";
    wheel.style.transform = `rotate(${finalAngle}deg)`;

    setTimeout(() => {{
      alert("🎯 Kết quả: " + items[selectedIndex]);
    }}, 5200);
  }}

  document.getElementById("spin").onclick = spinWheel;

  drawWheel();
</script>
"""

components.html(wheel_code, height=750)
