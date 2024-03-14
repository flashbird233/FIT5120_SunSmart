import streamlit as st
from streamlit_option_menu import option_menu

import sunscreen_set
import uv_data_impacts
import view_uv_level_locations


# Define a function to show the page header
def show_header():
    col1, col2, col3, col4 = st.columns([0.3, 0.1, 0.3, 0.3])
    with col2:
        st.image("./pic/SACA_logo2.jpg",
                 use_column_width=True)
    with col3:
        st.markdown("# Sun Smart")


# Define a function to show the page footer
def show_footer():
    st.markdown("""
    ---
    """)
    col1, col2 = st.columns([1, 1])
    with col1:
        show_about_us()
    with col2:
        show_more_links()


# Define a function to show the about us section
def show_about_us():
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
        st.image("./pic/SACA_logo2.jpg",
                 width=35)
    with col2:
        st.markdown("""
                    ##### About us:
                    """)
    st.write("""
    We are the SunSmart IT Team, a group of four individuals passionate about technology and innovation. 
    Dedicated to leveraging the latest web technologies, we aim to enhance public awareness and adoption of 
    the SunSmart concept. Through meticulous design and development, we have crafted this informative and 
    user-friendly platform. We hope our efforts will empower everyone to enjoy the sunshine while protecting 
    their skin health.
    """)


# Define a function to show more information links in the footer
def show_more_links():
    st.markdown("""
    ##### Learn More:
    """)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("[UV Radiation](https://en.wikipedia.org/wiki/Ultraviolet)")
        st.write("[Eye Damage by UV Light](https://www.aoa.org/patients-and-public/caring-for-your-vision"
                 "/uv-protection)")
        st.write("[Sun Protection](https://www.cancer.org.au/save-your-skin/five-sunsmart-steps)")
    with col2:
        st.write("[Skin Cancer](https://www.cancer.org.au/cancer-information/types-of-cancer/skin-cancer)")
        st.write("[Sunburn](https://www.mayoclinic.org/diseases-conditions/sunburn/symptoms-causes/syc-20355922)")
    with col3:
        st.write("[Sunscreen](https://en.wikipedia.org/wiki/Sunscreen)")
        st.write("[Premature Aging of the Skin](https://dermnetnz.org/topics/ageing-skin)")


# The main function
def main():
    # Simple navigation using the sidebar
    st.set_page_config(layout="wide",
                       page_title="Sun Smart",
                       menu_items=None)
    show_header()
    selected = option_menu(None,
                           ["Home", "---", "UV Check", "---", "Sunscreen Set"],
                           orientation="horizontal",
                           icons=["house", None, "search", None, "alarm-fill"])

    # Main logic
    if selected == 'Home':
        uv_data_impacts.show_data_main()
    elif selected == 'Sunscreen Set':
        sunscreen_set.sunscreen_set_main()
    elif selected == 'UV Check':
        view_uv_level_locations.view_uv_level_main()

    show_footer()


main()
