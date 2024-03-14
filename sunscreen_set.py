import streamlit as st
from datetime import datetime, timedelta, time


# Determine when to reapply sunscreen
def calculate_next_application_time(uv_index, application_time, location):
    if location == 'Indoors':
        return application_time + timedelta(hours=4)  # Indoors, reapply after 4-5 hours
    elif location == 'Outdoor':
        if uv_index <= 5:
            return application_time + timedelta(hours=3)  # Outdoor, UV index 0-5, reapply after 3-4 hours
        else:
            return application_time + timedelta(hours=1.5)  # Outdoors, with UV index above 6, reapply after 1.5 hours
    elif location == 'swimming':
        return application_time + timedelta(hours=1)  # For swimming, reapply every 1-2 hours
    else:
        return application_time  # If the location is ambiguous, the original time is returned


# User interface display function
def sunscreen_set_main():
    st.write('This is the sunscreen set page')
    st.write("Sun protection reminder")
    uv_index = st.number_input('please input the uv level：', min_value=0.0, value=11.0, step=0.1)

    # User selects hours and minutes
    # Select hours
    hour = st.slider("Hour", 0, 23, 0)

    # Select minutes
    minute = st.slider("Minute", 0, 59, 0)

    # Create a datetime.time object
    application_time_input = time(hour=hour, minute=minute)

    st.write('You selected:', application_time_input)
    location = st.selectbox('choose your location：', ['Indoor', 'Outdoor', 'swimming pool'])
    application_time = datetime.combine(datetime.today(), application_time_input)

    # Calculates and displays next application time
    next_application_time = calculate_next_application_time(uv_index, application_time, location)
    st.write(f"Depending on the UV index and your location, you should reapply sunscreen at this time：{next_application_time.time()}")

    # Determine whether it has reached the time point set by the user
    current_time = datetime.now().time()
    if current_time >= application_time_input:
        st.write("It's time to reapply sunscreen")
