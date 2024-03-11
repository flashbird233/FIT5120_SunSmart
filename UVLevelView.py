# UVLevelView.py
import streamlit as st
import DataCollect


def view_uv_level_main():
    st.title("View UV Index")

    # Check if the return button is pressed, if so, change the page state.
    if 'return_pressed' not in st.session_state:
        st.session_state.return_pressed = False

    if st.button('Return', key='return_from_uv_level_locations'):
        st.session_state.return_pressed = True
        st.session_state.current_page = 'home'

    # Only show the postcode and suburb input if the return button has not been pressed.
    if not st.session_state.return_pressed:
        postcode = st.text_input("Please input your postcode:")
        suburb = st.text_input("Please input your suburb")

        if st.button("Get UV level"):
            weather_info = DataCollect.get_weather_cur(postcode, suburb)
            temp = DataCollect.get_uv_level(weather_info)
            if temp:
                st.write(f"The UV index for {suburb} ({postcode}) is: {temp}")
            else:
                st.error("No location found for the given postcode and suburb.")
