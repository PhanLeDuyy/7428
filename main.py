import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="🎯 Vòng quay may mắn", layout="centered")
st.title("🎯 Vòng Quay May Mắn")

# HTML + CSS + JS code vòng quay (đã chỉnh sửa nhẹ cho phù hợp trong iframe)
wheel_code = """
<style>
  body {
    font-family: sans-serif;
    text-align: center;
    background: #f3f3f3;
    margin: 0; padding: 0;
  }
  #wheel {
    margin: 40px auto;
    width: 400px;
    height: 400px;
    border-radius: 50%;
    border: 10px solid #333;
    position: relative;
    overflow: hidden;
    box-shadow: 0 0 20px rgba(0,0,0,0.2);
    transform: rotate(0deg);
  }
  .segment {
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
  }
  #spin {
    margin-top: 20px;
    padding: 10px 20px;
    font-size: 20px;
    cursor: pointer;
  }
  #pointer {
    width: 0;
    height: 0;
    border-left: 20px solid transparent;
    border-right: 20px solid transparent;
    border-bottom: 30px solid red;
    position: absolute;
    top: -30px;
    left: calc(50% - 20px);
  }
</style>

<h1>🎯 Vòng Quay May Mắn</h1>
<div id="wheel">
  <div id="pointer"></div>
</div>
<button id="spin">QUAY</button>

<script>
  const items = ["A", "B", "C", "D"];
  const weights = [50, 20, 20, 10];
  const colors = ["#f44336", "#4caf50", "#2196f3", "#ff9800"];
  const wheel = document.getElementById("wheel");

  function drawWheel() {
    for (let i = 0; i < items.length; i++) {
      const segment = document.createElement("div");
      segment.className = "segment";
      segment.style.background = colors[i % colors.length];
      const angle = i * (360 / items.length);
      segment.style.transform = `rotate(${angle}deg)`;
      segment.innerHTML = items[i];
      wheel.appendChild(segment);
    }
  }

  function weightedChoice(items, weights) {
    const total = weights.reduce((a, b) => a + b, 0);
    const r = Math.random() * total;
    let sum = 0;
    for (let i = 0; i < items.length; i++) {
      sum += weights[i];
      if (r < sum) return i;
    }
  }

  function spinWheel() {
    const selectedIndex = weightedChoice(items, weights);
    const anglePerItem = 360 / items.length;
    const baseAngle = selectedIndex * anglePerItem;
    const extra = 360 * 5; // quay 5 vòng
    const finalAngle = extra + (360 - baseAngle - anglePerItem / 2);

    wheel.style.transition = "transform 5s ease-out";
    wheel.style.transform = `rotate(${finalAngle}deg)`;

    setTimeout(() => {
      alert("🎯 Kết quả: " + items[selectedIndex]);
    }, 5200);
  }

  document.getElementById("spin").onclick = spinWheel;

  drawWheel();
</script>
"""

# Nhúng HTML/JS vào Streamlit app, chiều cao đủ lớn để show wheel và button
html(wheel_code, height=600)

