import streamlit as st
from streamlit_option_menu import option_menu

import sunscreen_set
import uv_data_impacts
import view_uv_level_locations


# Define a function to show the page footer
def show_footer():
    st.markdown("""
    ---
    """)
    col1, col2 = st.columns([2, 4])
    with col1:
        st.markdown("""
        ##### About us
        """)
    with col2:
        show_more_links()


# Define a function to show more information links in the footer
def show_more_links():
    st.markdown("""
    ##### Learn More:
    """)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("[UV Radiation](https://en.wikipedia.org/wiki/Ultraviolet)")
        st.write("[Eye Damage by UV Light](https://www.aoa.org/patients-and-public/caring-for-your-vision"
                 "/uv-protection)")
    with col2:
        st.write("[Skin Cancer](https://www.cancer.org.au/cancer-information/types-of-cancer/skin-cancer)")
        st.write("[Sunburn](https://www.mayoclinic.org/diseases-conditions/sunburn/symptoms-causes/syc-20355922)")
    with col3:
        st.write("[Sunscreen](https://en.wikipedia.org/wiki/Sunscreen)")
        st.write("[Premature Aging of the Skin](https://dermnetnz.org/topics/ageing-skin)")
    with col4:
        st.write("[Sun Protection](https://dermnetnz.org/topics/sunburn)")


# The main function
def main():
    # Simple navigation using the sidebar
    st.set_page_config(layout="wide")
    selected = option_menu(None,
                           ["Home", "---", "UV Check", "---", "Sunscreen Set"],
                           orientation="horizontal")

    # Main logic
    if selected == 'Home':
        uv_data_impacts.show_data_main()
    elif selected == 'Sunscreen Set':
        sunscreen_set.sunscreen_set_main()
    elif selected == 'UV Check':
        view_uv_level_locations.view_uv_level_main()

    show_footer()


main()
