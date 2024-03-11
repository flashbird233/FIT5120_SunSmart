import streamlit as st


# This is the main app function.
def show_uv_impact():
    # Sets the page configuration to wide by default
    st.set_page_config(layout="wide")
    # Title of the app
    st.title('About UV Radiation')
    # Using columns to show the text, the image, and an empty column to push content to the left
    # Allocate more space to the image column by adjusting the ratio in the columns list
    col1, col2, col3 = st.columns([1, 1, 1])  # Adjust the middle number to give more space to the image

    # First column for text
    with col1:
        st.header('What is UV Radiation?')
        st.write("""
        UV (ultraviolet) radiation is a type of light from the sun that can be harmful to our skin. It's really strong in Australia, making skin cancer much more common there. UV radiation is bad because it can damage the skin and lead to serious types of skin cancer, including melanoma, which is very dangerous, as well as other kinds like basal cell and squamous cell carcinoma.

        Because of the strong UV radiation in Australia, a lot of people get skin cancer, especially if they get too much sun when they are young. This has made Australians more careful about protecting themselves from the sun. They are using sunscreen more, wearing hats, and covering up their skin to reduce the risk of getting cancer from UV radiation. Staying safe from the sun's harmful rays is really important to keep skin healthy.
        """)

        st.header('Health Risks Related with UV Radiation')
        st.write("Skin Cancer")
        st.write("Sunburn (Erythema)")
        st.write("Premature Aging of the Skin")
        st.write("Eye Damage")

    # Second column for text
    with col2:
        st.header('Protective Measures Against UV Radiation')
        st.write("Seek shade, particularly when the sun is strongest (midday).")
        st.write("Dress in clothing that covers your arms and legs.")
        st.write("Take extra steps to shield your kids from the sun.")
        st.write("Use a wide-brimmed hat to protect your face, head, ears and neck.")
        st.write("Choose sunglasses that cover all angles and block UVA and UVB rays.")
        st.write("Apply sunscreen with at least SPF 15, guarding against both UVA and UVB rays.")
        st.write("Steer clear of indoor tanning.")

    # Third column for image
    with col3:
        st.image("SunImpact.png")

    if st.button('Return', key='return_from_uv_data_impacts'):
        st.session_state.current_page = 'home'


# The following is Streamlit way to run the app function when the script is run.
if __name__ == "__main__":
    show_uv_impact()
