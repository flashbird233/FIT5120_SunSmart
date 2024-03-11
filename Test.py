# This is a test file

import streamlit as st


def set_page_status(page_name):
    st.session_state.current_page = page_name


def show_main_page():
    # Show the main page
    st.header('Welcome to the sun protection page')


def main():
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'home'

    if st.session_state.current_page == 'home':
        show_main_page()


if __name__ == "__main__":
    main()
