import streamlit as st

import view_uv_level_locations, uv_data_impacts, sunscreen_set

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
    st.sidebar.title('Navigation')
    choice = st.sidebar.radio('Which page to go to?', ('home page', 'sunscreen_set', 'uv level'))

    # Main logic
    if choice == 'home page':
        home_page()
    elif choice == 'sunscreen_set':
        page2()
    elif choice == 'uv level':
        page3()


main()
