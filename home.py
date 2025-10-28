import streamlit as st
import time

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Ocean Safe",
    page_icon="🏖️",
    layout="wide"
)

# ---------------------------
# Loader Animation (MP4)
# ---------------------------
loader_placeholder = st.empty()

# Play MP4 loader animation
loader_placeholder.video("wave_animation.mp4")  # <-- replace with your file path

# Simulate loading time (replace with actual data fetching if needed)
time.sleep(3)

# Remove loader
loader_placeholder.empty()

# ---------------------------
# Hero Section
# ---------------------------
st.markdown("""
<div style='position: relative; text-align: center; color: white; margin-bottom: 30px;'>
    <h1 style='font-size: 3em; margin-bottom: 0;'>Beach Safety Chatbot 🏖️</h1>
    <p style='font-size: 1.2em; margin-top: 0;'>Your intelligent companion for safe beach adventures!</p>
</div>
""", unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&h=400&fit=crop",
    use_container_width=True,
    caption="Stay Safe at the Beach"
)

# ---------------------------
# About Section using Tabs
# ---------------------------
st.markdown("<br>", unsafe_allow_html=True)
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

# ---------------------------
# Footer
# ---------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Stay safe, stay informed, enjoy the beach! 🌴</p>",
    unsafe_allow_html=True
)
