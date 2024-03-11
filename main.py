import streamlit as st

import UVImpact
import UVLevelView


# https://api.openweathermap.org/data/3.0/onecall?lat=39.099724&lon=-94.578331&exclude=hourly,daily,minutely,alerts&appid=eb91e203d9a036e297d76e0d4e7336b0
def set_page_status(page_name):
    st.session_state.current_page = page_name


def show_main_page():
    # Show the main page
    st.header('Welcome to the sun protection page')
    if st.button('UV Level Locations', key='uv_level_locations_btn'):
        set_page_status('view_uv_level_locations')
    elif st.button('Data about UV impacts', key='uv_data_impacts'):
        set_page_status('uv_data_impacts')


def main():
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'home'

    if st.session_state.current_page == 'home':
        show_main_page()
    elif st.session_state.current_page == 'view_uv_level_locations':
        UVLevelView.view_uv_level_main()
    elif st.session_state.current_page == 'uv_data_impacts':
        UVImpact.show_uv_impact()


main()
