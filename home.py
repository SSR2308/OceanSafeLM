import streamlit as st


st.set_page_config(
    page_title="Beach Safety Hazards Chatbot",
    page_icon="🏖️",
    layout="wide"
)

st.title("Beach Saftey Chatbot")

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# Display beach image (using a placeholder URL - you can replace with your own image)
st.image(
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&h=400&fit=crop",
    use_container_width=True,
    caption="Stay Safe at the Beach"
)
