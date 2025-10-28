import streamlit as st

st.set_page_config(
    page_title="Ocean Safe",
    page_icon="🏖️",
    layout="wide"
)

# Inject CSS
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Hero
st.markdown("""
<div style='text-align: center; color: #fff; background-color: #0b3d91; padding: 40px; border-radius: 15px;'>
    <h1 style='font-size: 3em; margin-bottom: 0;'>Beach Safety Chatbot 🏖️</h1>
    <p style='font-size: 1.2em; margin-top: 0;'>Your intelligent companion for safe beach adventures!</p>
</div>
""", unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&h=400&fit=crop",
    use_container_width=True,
    caption="Stay Safe at the Beach"
)

# Wave animation
st.markdown('<div class="wave"></div>', unsafe_allow_html=True)

# Cards layout
st.markdown("<div style='display: flex; flex-wrap: wrap; gap: 20px;'>", unsafe_allow_html=True)

cards = [
    {"title": "🌟 Overview", "content": "Welcome to **Ocean Safe**. Ask Tidebot any beach-related questions and get accurate safety info! Explore weather, tide patterns, hazards, and navigation to beaches."},
    {"title": "🚨 Features", "content": "• Temperature, Weather & UV forecasts\n• Tide patterns for the day\n• Live hazard reports\n• Live navigation to beaches"},
    {"title": "💡 Tidebot Helps You", "content": "• Identify potential hazards\n• Get instant answers to beach safety questions\n• Learn about water & marine life safety\n• Sun protection tips\n• Emergency advice for beach incidents"}
]

for card in cards:
    st.markdown(f"""
    <div class="card" style="flex: 1 1 30%;">
        <h3>{card['title']}</h3>
        <p>{card['content'].replace(chr(10), '<br>')}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Stay safe, stay informed, enjoy the beach! 🌴</p>",
    unsafe_allow_html=True
)
