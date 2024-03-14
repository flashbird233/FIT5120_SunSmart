import streamlit as st

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('切换按钮', on_click=click_button)

if st.session_state.button:
    st.slider('显示或隐藏的滑动条')

