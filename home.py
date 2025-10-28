import streamlit as st
import time

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Ocean Safe",
    page_icon="🏖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------
# Adjustable numeric variables
# ---------------------------
VIDEO_WIDTH = 0.9          # 0.0 - 1.0 (percentage of screen width)
VIDEO_MAX_HEIGHT = 0.75    # 0.0 - 1.0 (percentage of screen height)
VIDEO_Y_OFFSET = 0.2       # -1.0 (up) to 1.0 (down), relative to center
TEXT_BOTTOM = 40           # px from bottom
TEXT_RIGHT = 30            # px from right
TEXT_SIZE = 7              # em

# ---------------------------
# Fullscreen Splash Animation with Text
# ---------------------------
video_url = "https://github.com/SSR2308/OceanSafeLM/blob/9761d751ca32b424d92cc29eba0c179d212e7127/bc8c-f169-4534-a82d-acc2fad66609.mp4?raw=true"

splash_container = st.empty()
splash_container.markdown(f"""
<div id="splash" style="
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: white;
    z-index: 9999;
    animation: fadeout 1s ease 4s forwards;
">

    <!-- Centered Video -->
    <video autoplay muted playsinline style="
        position: absolute;
        top: calc(50% + {VIDEO_Y_OFFSET * 100}%);
        left: 50%;
        transform: translate(-50%, -50%);
        width: {VIDEO_WIDTH * 100}%;
        height: auto;
        max-height: {VIDEO_MAX_HEIGHT * 100}%;
    ">
        <source src="{video_url}" type="video/mp4">
        Your browser does not support the video tag.
    </video>

    <!-- Bottom-right Text -->
    <h1 style='
        position: absolute;
        bottom: {TEXT_BOTTOM}px;
        right: {TEXT_RIGHT}px;
        font-family: "Brush Script MT", cursive;
        font-size: {TEXT_SIZE}em;
        color: #0077be;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
    '>
        Ocean Safe
    </h1>

</div>

<style>
@keyframes fadeout {{
    to {{
        opacity: 0;
        visibility: hidden;
    }}
}}
</style>
""", unsafe_allow_html=True)

time.sleep(5)
splash_container.empty()

# ---------------------------
# Sidebar Content
# ---------------------------
st.sidebar.header("Navigation")
st.sidebar.info("Select a page to explore!")

# ---------------------------
# Main Content
# ---------------------------
st.markdown("""
<div style='text-align: center; color: white;'>
    <h1 style='font-size: 3em;'>Beach Safety Chatbot 🏖️</h1>
    <p style='font-size: 1.2em;'>Your intelligent companion for safe beach adventures!</p>
</div>
""", unsafe_allow_html=True)

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

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Stay safe, stay informed, enjoy the beach! 🌴</p>",
    unsafe_allow_html=True
)
