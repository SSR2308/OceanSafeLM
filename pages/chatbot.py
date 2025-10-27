import streamlit as st 
from rag import response_generator 

st.title("Ocean Safety Chatbot") 

if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages: 
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

if prompt := st.chat_input("What's up?"):
  st.markdown("Hi") 
