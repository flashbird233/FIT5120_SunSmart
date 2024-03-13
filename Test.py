# This is a test file

import streamlit as st
from streamlit_option_menu import option_menu
# 创建菜单栏
selected = option_menu(None,
                       ["Home", "Sunscreen Set", "UV Level"],
                       orientation="horizontal")

if selected == "Home":
    st.title("Home")
    st.write("This is the home page")
elif selected == "Sunscreen Set":
    st.title("Sunscreen Set")
    st.write("This is the sunscreen set page")
