import streamlit as st


# This is the main app function.
def show_data_main():
    # Using columns to lay out the text, the image, and an empty column to push content to the left
    # Allocate more space to the image column by adjusting the ratio in the columns list
    col1, col2 = st.columns([0.6, 0.4])  # Adjust the middle number to give more space to the image
    # First column for text
    with col1:
        st.header('What is UV Radiation?')
        st.write("""
                UV (ultraviolet) radiation is a type of light from the sun that can be harmful to our skin. 
                It's really strong in Australia, making skin cancer much more common there. UV radiation is bad 
                because it can damage the skin and lead to serious types of skin cancer, including melanoma, 
                which is very dangerous, as well as other kinds like basal cell and squamous cell carcinoma.
        
                Because of the strong UV radiation in Australia, a lot of people get skin cancer, especially 
                if they get too much sun when they are young. This has made Australians more careful about 
                protecting themselves from the sun. They are using sunscreen more, wearing hats, and 
                covering up their skin to reduce the risk of getting cancer from UV radiation. 
                Staying safe from the sun's harmful rays is really important to keep skin healthy.
        """)

    # Second column for text
    with col2:
        st.image("./pic/SunImpact.png")
    st.write('---')

    col1, col2 = st.columns([0.6, 0.4])

    with col1:
        st.header('Protective Measures Against UV Radiation')
        st.write("""
                When summer comes with scorching heat and intense sunlight, especially during the peak of the 
                day when the sun is at its strongest, seeking shade is of utmost importance. Finding a spot under 
                a tree or the protection of an umbrella can help you avoid prolonged exposure to direct sunlight.
                
                When it comes to clothing, wearing attire that covers your arms and legs is a wise choice. Opting 
                for lightweight and breathable long-sleeved shirts and pants can not only prevent direct sunlight 
                from reaching your skin but also effectively reduce sweat secretion, keeping you cool and 
                comfortable in the sweltering heat.
                
                For children, their skin is even more delicate, so we need to pay extra attention to their sun 
                protection. Prepare special children's sunscreen for them and ensure they apply it regularly. 
                Additionally, avoid taking them out during peak hours to further safeguard them from the sun's 
                harmful rays.
                
                A wide-brimmed hat is not only a fashion statement but also a valuable ally in sun protection. 
                It effectively shields your face, head, ears, and neck from the sun's rays, reducing the risk 
                of UV damage to your skin.
                
                When choosing sunglasses, it's crucial to select ones that cover all angles and block both UVA 
                and UVB rays. Such sunglasses can protect your eyes from the harmful effects of UV light, giving 
                you peace of mind when engaging in outdoor activities.
                
                Applying sunscreen is also a crucial step in sun protection. Choose a sunscreen with an SPF of 
                at least 15 that guards against both UVA and UVB rays. Apply it half an hour before going outdoors 
                and reapply regularly to maintain its effectiveness.
                """)

    with col2:
        st.image("./pic/picc.jpg")

    st.write('---')

    st.image("./pic/five_way_prot.png")
