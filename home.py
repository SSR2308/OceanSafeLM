import streamlit as st
import time

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Ocean Safe",
    page_icon="🏖️",
    layout="wide",
    initial_sidebar_state="collapsed"  # hide sidebar during splash
)

# ---------------------------
# Fullscreen Splash Animation
# ---------------------------
splash_container = st.empty()

# GitHub raw link for MP4
video_url = "https://github.com/SSR2308/OceanSafeLM/blob/9761d751ca32b424d92cc29eba0c179d212e7127/bc8c-f169-4534-a82d-acc2fad66609.mp4?raw=true"

splash_container.markdown(f"""
<div id="splash" style="
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: white;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 9999;
    transition: opacity 1s ease;
">
    <video autoplay muted playsinline style="max-width: 80%; max-height: 80%;">
        <source src="{video_url}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>

<script>
    // Fade out splash after video duration (replace 5 with your video seconds)
    setTimeout(() => {{
        const splash = document.getElementById('splash');
        splash.style.opacity = '0';
        setTimeout(() => splash.remove(), 1000);
    }}, 5000);
</script>
""", unsafe_allow_html=True)

# ---------------------------
# Main Homepage Content
# ---------------------------
# Inject custom CSS for cards and styling
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Make all text white
st.markdown("""
<style>
body, .stApp, h1, h2, h3, p, .stMarkdown {
    color: white !important;
}
.stApp {
    background-color: #000000;  /* Optional: black background */
}
</style>
""", unsafe_allow_html=True)

# Show sidebar now (optional)
st.sidebar.header("Navigation")
st.sidebar.info("Select a page to explore!")

# Hero section
st.markdown("""
<div style='position: relative; text-align: center; color: white;'>
    <h1 style='font-size: 3em; margin-bottom: 0;'>Beach Safety Chatbot 🏖️</h1>
    <p style='font-size: 1.2em; margin-top: 0;'>Your intelligent companion for safe beach adventures!</p>
</div>
""", unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&h=400&fit=crop",
    use_container_width=True,
    caption="Stay Safe at the Beach"
)

# About section using tabs
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

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: white;'>Stay safe, stay informed, enjoy the beach! 🌴</p>",
    unsafe_allow_html=True
)
