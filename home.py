import streamlit as st

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
video_url = "https://github.com/SSR2308/OceanSafeLM/blob/9761d751ca32b424d92cc29eba0c179d212e7127/bc8c-f169-4534-a82d-acc2fad66609.mp4?raw=true"

st.markdown(f"""
<style>
/* Initially hide sidebar */
[data-testid="stSidebar"] {{
    display: none !important;
}}

/* Splash fullscreen container */
#splash {{
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
    animation: fadeout 1s ease 4s forwards; /* fade after 4s */
}}

/* Video inside splash */
#splash video {{
    max-width: 80%;
    max-height: 80%;
}}

/* Fade-out animation */
@keyframes fadeout {{
    to {{
        opacity: 0;
        visibility: hidden;
    }}
}}

/* Hamburger toggle button */
#toggleSidebar {{
    position: fixed;
    top: 20px;
    left: 20px;
    z-index: 10000;
    width: 35px;
    height: 30px;
    cursor: pointer;
}}

#toggleSidebar div {{
    width: 100%;
    height: 5px;
    background-color: #023e8a;
    margin: 6px 0;
    transition: 0.4s;
}}
</style>

<!-- Splash container -->
<div id="splash">
    <video autoplay muted playsinline>
        <source src="{video_url}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>

<!-- Hamburger button -->
<div id="toggleSidebar" onclick="toggleSidebar()">
  <div></div>
  <div></div>
  <div></div>
</div>

<script>
// Remove splash after video duration and fade
setTimeout(function(){{
    var splash = document.getElementById("splash");
    if(splash) splash.remove();
}}, 5000);

// Function to toggle sidebar
function toggleSidebar() {{
    const sidebar = document.querySelector('[data-testid="stSidebar"]');
    if(sidebar) {{
        if(sidebar.style.display === 'block') {{
            sidebar.style.display = 'none';
        }} else {{
            sidebar.style.display = 'block';
        }}
    }}
}}
</script>
""", unsafe_allow_html=True)

# ---------------------------
# Main Homepage Content
# ---------------------------
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

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
    "<p style='text-align: center; color: gray;'>Stay safe, stay informed, enjoy the beach! 🌴</p>",
    unsafe_allow_html=True
)
