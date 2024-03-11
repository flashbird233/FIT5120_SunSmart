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

        if st.button("Get UV level"):
            weather_info = DataCollect.get_weather_cur(postcode)
            uvl = DataCollect.get_uv_level(weather_info)
            suburb = DataCollect.get_suburb(postcode)
            if suburb:
                st.write(f"The UV index for {suburb} is: {uvl}")
                st.title("Suggestions")
                sug = DataCollect.get_spf_sug(uvl)
                st.write(sug)
            else:
                st.error("No location found for the given postcode and suburb.")
