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
# Fullscreen Splash Animation
# ---------------------------
splash_container = st.empty()

video_url = "https://github.com/SSR2308/OceanSafeLM/blob/9761d751ca32b424d92cc29eba0c179d212e7127/bc8c-f169-4534-a82d-acc2fad66609.mp4?raw=true"

# Make video fullscreen, remove scrollbars and default blue styling
splash_container.markdown(f"""
<style>
body {{
    margin: 0;
    overflow: hidden; /* remove scroll */
    background-color: white; /* white background */
}}
.stApp {{
    background-color: white;
}}
</style>

<div style="
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: white;
    z-index: 9999;
">
    <video autoplay muted playsinline style="width:100vw; height:100vh; object-fit:cover;">
        <source src="{video_url}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>
""", unsafe_allow_html=True)

# Wait for video duration (adjust seconds to match your video)
time.sleep(5)

# Remove splash
splash_container.empty()

# ---------------------------
# Main Homepage Content
# ---------------------------
# Inject custom CSS for cards, styling, remove default Streamlit colors
st.markdown("""
<style>
body { background-color: white; }
.stApp { background-color: white; }
h1, h2, h3, p { color: #023e8a; } /* change headings to dark blue */
</style>
""", unsafe_allow_html=True)

# Optional sidebar
st.sidebar.header("Navigation")
st.sidebar.info("Select a page to explore!")

# Hero section
st.markdown("""
<div style='text-align: center;'>
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
    "<p style='text-align: center; color: gray;'>Stay safe, stay informed, enjoy the beach! 🌴</p>",
    unsafe_allow_html=True
)
