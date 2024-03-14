# UVLevelView.py
import streamlit as st
import DataCollect


def view_uv_level_main():
    st.image("./pic/sunshine.jpg")
    st.title("View UV Index")

    postcode = st.text_input("Please input your postcode:")

    if st.button("Get UV level"):
        weather_info = DataCollect.get_weather_cur(postcode)
        uvl = DataCollect.get_uv_level(weather_info)
        # uvl=10
        suburb = DataCollect.get_suburb(postcode)
        if suburb:
            st.write(f"The UV index for {suburb} is: {uvl}")
            st.header("Suggestions")
            sug, cloth_sug, suns_sug = DataCollect.get_spf_sug(uvl)
            st.write(sug)
            if cloth_sug:
                # Split to columns
                col1, col2 = st.columns(2)
                with col1:
                    st.header("Clothing Required:")
                    st.write(cloth_sug)
                with col2:
                    st.header("Sunscreen Required:")
                    st.write(suns_sug)
        else:
            st.error("No location found for the given postcode and suburb.")
    st.image("./pic/UVL_prot.jpg")
