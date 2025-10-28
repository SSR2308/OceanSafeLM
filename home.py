import streamlit as st
import time

st.set_page_config(page_title="Ocean Safe", page_icon="🏖️", layout="wide")

# Fullscreen video loader
loader_placeholder = st.empty()

loader_html = """
<div style="
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
">
    <video autoplay muted playsinline style="max-width: 80%; max-height: 80%;">
        <source src="bc8c-f169-4534-a82d-acc2fad66609.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>
"""

loader_placeholder.markdown(loader_html, unsafe_allow_html=True)

# Simulate loading (or wait for video duration)
time.sleep(3.5)  # Adjust to the length of your video

loader_placeholder.empty()

# ---- Main page content ----
st.title("Beach Safety Chatbot 🏖️")

st.image(
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&h=400&fit=crop",
    use_container_width=True,
    caption="Stay Safe at the Beach"
)

tabs = st.tabs(["🌟 Overview", "🚨 Features", "💡 Tidebot Helps You"])

with tabs[0]:
    st.markdown("""
    Welcome to **Ocean Safe**. Ask Tidebot any beach-related questions and get accurate safety info!
    Explore weather, tide patterns, hazards, and navigation to beaches.
    """)

with tabs[1]:
    st.markdown("""
    **Features Include:**  
    - 🌡 Temperature, Weather & UV forecasts  
    - 🌊 Tide patterns for the day  
    - 🚨 Live hazard reports  
    - 🗺 Live navigation to beaches
    """)

with tabs[2]:
    st.markdown("""
    **Tidebot Helps You:**  
    - 🚨 Identify potential hazards  
    - 💡 Get instant answers to beach safety questions  
    - 🏊 Learn about water & marine life safety  
    - ☀️ Sun protection tips  
    - 🆘 Emergency advice for beach incidents
    """)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Stay safe, stay informed, enjoy the beach! 🌴</p>",
    unsafe_allow_html=True
)
