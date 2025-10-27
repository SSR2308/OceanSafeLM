import streamlit as st



st.set_page_config(
    page_title="Ocean Safe",
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

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# About section
st.header("🌊 What is this about?")


st.markdown("""
Welcome to the **Ocean Safe**, please explore and direct beach-related questions to Tidebot- your intelligent companion for beach safety information!

Please visit the Beach Dashboard to find out: 

- Check Tempreture
- Check the Weather
- Check the UVs 
- Understand the tides and the tide pattern throughout the day 
- Report and receive live hazard updates
- Receive live navigation to the Beaches

Tidebot is designed to help you:

- 🚨 **Identify potential beach hazards** and understand the risks
- 💡 **Get instant answers** to your beach safety questions
- 🏊 **Learn about water safety**, rip currents, and swimming conditions
- 🐚 **Understand marine life hazards** like jellyfish, stingrays, and more
- ☀️ **Receive sun protection tips** and weather-related safety advice
- 🆘 **Know what to do in emergencies** at the beach

Simply ask any question about beach safety, and our AI-powered chatbot will provide you with 
accurate, helpful information to ensure you have a safe and enjoyable beach experience!
""")

# Call to action
st.markdown("<br>", unsafe_allow_html=True)
st.info("👈 Navigate to the **Chatbot** page from the sidebar to start asking questions!")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Stay safe, stay informed, enjoy the beach! 🌴</p>",
    unsafe_allow_html=True
)
