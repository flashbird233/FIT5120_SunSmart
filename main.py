import streamlit as st
import requests


# Test for Streamlit
st.title('Hello World')
st.write('This is a simple Streamlit app.')

# Test for requests
lat = -37.8136
lon = 144.9631
key = "d32542473437f300dfdec104552b7f65"
main_url = "https://api.openweathermap.org/data/3.0/onecall?"
req_url = main_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + key
# Get the UV level
response = requests.get(req_url)
st.write(response.json())

