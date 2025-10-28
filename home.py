import streamlit as st

st.set_page_config(
    page_title="Ocean Safe",
    page_icon="🏖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Splash Screen with Animation ---
splash_html = """
<style>
/* Fullscreen white background for splash */
#splash {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
}
#splash video {
    max-width: 80%;
    max-height: 80%;
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
}
body {
    overflow: hidden; /* Disable scroll while splash */
}
</style>

<div id="splash">
    <video id="splashVideo" autoplay muted playsinline>
        <source src="https://github.com/SSR2308/OceanSafeLM/blob/9761d751ca32b424d92cc29eba0c179d212e7127/bc8c-f169-4534-a82d-acc2fad66609.mp4?raw=true" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>

<script>
var video = document.getElementById('splashVideo');
video.onended = function() {
    var splash = document.getElementById('splash');
    splash.style.display = 'none';
    document.body.style.overflow = 'auto';  // Re-enable scrolling after splash
};
</script>
"""

st.markdown(splash_html, unsafe_allow_html=True)

# --- Main Homepage Content ---
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Hero section
st.markdown("""
<div style='position: relative; text-align: center; color: #1e3f66;'>
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

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Stay safe, stay informed, enjoy the beach! 🌴</p>",
    unsafe_allow_html=True
)
