from weatherapi import get_weather_data 
import streamlit as st
long = st.text_input("Can you please tell us longitude")
lat = st.text_input("Can you please tell us lattitude")
response = get_weather_data(lat, long)
response = str(response)
st.markdown(response) 



