import streamlit as st
import time

st.set_page_config(
    page_title="Ocean Safe",
    page_icon="🏖️",
    layout="wide"
)

# Inject CSS
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Placeholder for loader
loader_placeholder = st.empty()

# Show loader
loader_placeholder.markdown("""
<div class="loader-overlay">
    <div class="loader"></div>
</div>
""", unsafe_allow_html=True)

# Simulate loading (replace with actual initialization if needed)
time.sleep(2)  # <-- time loader is visible

# Remove loader
loader_placeholder.empty()

# Now render the actual homepage content
st.title("Beach Safety Chatbot 🏖️")
st.image(
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&h=400&fit=crop",
    use_container_width=True,
    caption="Stay Safe at the Beach"
)
st.markdown('<div class="wave"></div>', unsafe_allow_html=True)

# ... rest of your homepage content ...
