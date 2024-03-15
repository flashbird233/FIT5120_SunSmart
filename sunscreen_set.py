import streamlit as st
import plotly.graph_objs as go
from datetime import datetime, timedelta, time


# Define the maximum UV index values for each level, their corresponding colors, and hover information
uv_levels = {
    "Level 1": {"max_index": 2, "color": "#FFD700", "action": "No protective measures required"},  # Light gold
    "Level 2": {"max_index": 4, "color": "#FFC300", "action": "You can take appropriate protective measures such as "
                                                              "applying sunscreen, etc."},  # Gold
    "Level 3": {"max_index": 6, "color": "#FF8C00", "action": "Wear a sun hat, sunglasses and umbrella when going out, "
                                                              "and apply sunscreen with an SPF index greater than 15"},
    "Level 4": {"max_index": 9, "color": "#FF4500", "action": "AIn addition to the above protective measures, avoid "
                                                              "going out from 10 a.m. to 4 p.m., or stay in the shade "
                                                              "as much as possible"},  # Dark orange-red
    "Level 5": {"max_index": 11, "color": "#DC143C", "action": "Try not to do outdoor activities as much as possible. "
                                                               "When you must go out, you need to take various "
                                                               "effective precautions."}  # Deep red
}


# Create an interactive bar chart
def create_interactive_bar(uv_levels):
    fig = go.Figure()

    for level, details in uv_levels.items():
        fig.add_trace(go.Bar(
            x=[level],  # Protection level as the X-axis
            y=[details["max_index"]],  # Use the maximum UV index value as the Y-axis value
            hoverinfo="text",
            hovertext=f"{level}: {details['action']}",  # Display protection measures on hover
            marker=dict(color=details["color"]),  # Use specified color for the bar
        ))

    # Set the layout for the chart
    fig.update_layout(
        title='UV Index Protective Measures',
        xaxis_title="Protection Level",
        yaxis=dict(title="Max UV Index", range=[0, 12]),  # Ensure Y-axis range covers all UV index values
        barmode='group'
    )

    return fig


# Calculate the next time the user should reapply sunscreen based on their location and last application time.
def calculate_next_application_time(application_time, location):
    if location == 'Indoor':
        return application_time + timedelta(hours=4)  # Reapply every 4 hours if indoors
    elif location == 'Outdoor':
        return application_time + timedelta(hours=2)  # Reapply every 2 hours if outdoors
    elif location == 'Swimming pool':
        return application_time + timedelta(hours=1)  # Reapply every hour if at a swimming pool
    else:
        return application_time  # If the location is unknown, return the last application time


# Check if the next application time is within the reminder window (10 AM to 5 PM).
def is_within_reminder_time(next_application_time):
    # Define the reminder time range
    reminder_start_time = time(10, 0)  # Start time at 10 AM
    reminder_end_time = time(17, 0)    # End time at 5 PM
    # Check if the next application time is within the reminder range
    return reminder_start_time <= next_application_time.time() <= reminder_end_time


# Set the background image for the app.
def add_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://th.bing.com/th/id/R.b6bac95ccc4d3baa449fef5e5ebb799d?rik=gACprKno0s1xQw&riu=http%3a%2f%2fst.gdefon.com%2fwallpapers_original%2f537108_peyzaj_more_bungalo_5295x3530_www.Gde-Fon.com.jpg&ehk=Ff6hkzM0%2f1Lw7tfVHSOjO9rMRNBYd2IKV2fMvvwtP6E%3d&risl=&pid=ImgRaw&r=0.jpg");
            background-size: cover;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True  # Allow HTML for styling purposes
    )


# The main sunscreen reminder set up.
def sunscreen_set():
    st.text(" ")  # Add a space for formatting purposes
    colored_text = '<p style="color: #FFD700; font-weight: bold;">Please choose the time when you first apply sunscreen:</p>'

    st.markdown(colored_text, unsafe_allow_html=True)

    # Input for the time of first sunscreen application without a label
    application_time_input = st.time_input('', value=time(10, 0))

    # st.write('Application time selected:', application_time_input)
    st.markdown('**Application time selected:** ' + str(application_time_input))

    # Let the user choose their location
    location = st.selectbox('Choose your location:', ['Indoor', 'Outdoor', 'Swimming pool'])

    # Calculate the next time to apply sunscreen based on the input time and location
    application_time = datetime.combine(datetime.today(), application_time_input)
    next_application_time = calculate_next_application_time(application_time, location)

    # Display reminder if it's within the reminder time range
    if is_within_reminder_time(next_application_time):
        next_app_time_text = f"Depending on your location, you should reapply sunscreen at: {next_application_time.time()}"
        st.markdown(f"<b style='color: #FFD700;'>{next_app_time_text}</b>", unsafe_allow_html=True)

        # Inform the user if it's time to reapply sunscreen
        if datetime.now() >= next_application_time:
            st.info("It's time to reapply sunscreen")
        else:
            st.info("You don't need to reapply sunscreen just yet.")
    else:
        # No need to apply sunscreen right now
        st.write("No need to reapply sunscreen at the moment. You're all set for now!")
# Main function to set up the Streamlit app layout.
def sunscreen_set_main():
    st.title('Sunscreen Reapplication Reminder')
    # add_background()

    # Set up a three-column layout
    col1, col2= st.columns([1, 1])
    with col1:
        sunscreen_set()  # Set up the sunscreen reminder in the first column
    #
    # with col2:
    #     pass  # Reserved for future content

    with col2:
        # Display the chart in Streamlit
        fig = create_interactive_bar(uv_levels)
        st.plotly_chart(fig)


