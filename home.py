import streamlit as st

st.set_page_config(
    page_title="Ocean Safe",
    page_icon="🏖️",
    layout="wide"
)

# Inject custom CSS for waves and styling
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
    use_column_width=True,
    caption="Stay Safe at the Beach"
)

# Wave animation div
st.markdown('<div class="wave"></div>', unsafe_allow_html=True)

# About section
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="info-card">
<h2>🌊 What is this about?</h2>
<p>Welcome to <strong>Ocean Safe</strong>. Ask Tidebot any beach-related questions and get:</p>
<ul>
<li>🌡 Temperature, Weather & UV forecasts</li>
<li>🌊 Tide patterns for the day</li>
<li>🚨 Live hazard reports</li>
<li>🗺 Live navigation to beaches</li>
</ul>
<p>Tidebot helps you:</p>
<ul>
<li>🚨 Identify hazards</li>
<li>💡 Get instant safety info</li>
<li>🏊 Learn water & marine life safety</li>
<li>☀️ Sun protection tips</li>
<li>🆘 Emergency advice</li>
</ul>
</div>
""", unsafe_allow_html=True)

# CTA Button
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center;'>
<a href='/Beach Dashboard' class='cta-button'>Go to Beach Dashboard 🌴</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Stay safe, stay informed, enjoy the beach! 🌴</p>",
    unsafe_allow_html=True
)
