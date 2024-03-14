import streamlit as st
from streamlit_option_menu import option_menu

import sunscreen_set
import uv_data_impacts
import view_uv_level_locations


# st.set_page_config(layout="wide")
def home_page():
    uv_data_impacts.show_data_main()


def page2():
    st.write('This is the sunscreen set page')
    sunscreen_set.sunscreen_set_main()


def page3():
    view_uv_level_locations.view_uv_level_main()


# The main function
def main():
    # Simple navigation using the sidebar
    st.set_page_config(layout="wide")
    selected = option_menu(None,
                           ["Home", "---", "UV Check", "---", "Sunscreen Set"],
                           orientation="horizontal")

    # Main logic
    if selected == 'Home':
        home_page()
    elif selected == 'Sunscreen Set':
        page2()
    elif selected == 'UV Check':
        page3()


main()
