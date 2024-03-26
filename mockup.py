import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import time

# Set page title and favicon
st.set_page_config(page_title="Healthcare Investment Experiment", page_icon=":hospital:")

# Define initial values
max_time = 100
initial_health = 50
initial_enjoyment = 50
shock_probability = 0.1
shock_impact = 20

# Define function to update health and enjoyment based on time allocation
def update_values(health_time, enjoyment_time, shock_probability):
    shock_event = np.random.choice(["none", "small", "large", "death"], p=[1-shock_probability, shock_probability/3, shock_probability/3, shock_probability/3])
    if shock_event == "small":
        health_impact = shock_impact / 2
    elif shock_event == "large":
        health_impact = shock_impact
    elif shock_event == "death":
        health_impact = initial_health  # Simulates death by setting health to 0
    else:
        health_impact = 0
    health = max(0, initial_health + health_time - health_impact)  # Ensure health doesn't go below 0
    enjoyment = initial_enjoyment + enjoyment_time
    return health, enjoyment, shock_event

# Set up the Streamlit app layout
st.title("Healthcare Investment Experiment")

st.markdown("""
Welcome to the Healthcare Investment Experiment! In this simulation, you will allocate your time between health and enjoyment activities to maximize your overall well-being.

- Use the sliders to allocate your time between health and enjoyment.
- The probability of health shocks increases over time.
- Monitor your health and enjoyment levels in real-time.
- Run the simulation to see how your choices impact your well-being.
""")

# Create sliders for time allocation
health_time = st.slider("Time allocated to health activities", min_value=0, max_value=max_time, value=50, step=10)
enjoyment_time = max_time - health_time

# Display current time allocation
st.write(f"Current time allocation: Health - {health_time}, Enjoyment - {enjoyment_time}")

# Create placeholders for health and enjoyment bars
health_bar = st.empty()
enjoyment_bar = st.empty()

# Placeholder for shock event notification
shock_event_placeholder = st.empty()

# Create a button to run the simulation
if st.button("Run Simulation"):
    # Initialize variables for tracking progress
    health = initial_health
    enjoyment = initial_enjoyment
    time_elapsed = 0
    health_data = []
    enjoyment_data = []
    consecutive_enjoyment = 0  # Initialize or update your logic for tracking consecutive enjoyment

    # Run the simulation
    while time_elapsed < max_time:
        # Update health and enjoyment based on time allocation
        health, enjoyment, shock_event = update_values(health_time, enjoyment_time, shock_probability)
        
        # Store data for plotting
        health_data.append(health)
        enjoyment_data.append(enjoyment)
        
        # Update health and enjoyment bars
        health_bar.progress(health)
        enjoyment_bar.progress(enjoyment)
        
        # Display numerical values and shock events
        st.write(f"Health: {health}, Enjoyment: {enjoyment}")
        if shock_event != "none":
            shock_event_placeholder.error(f"Shock Event: {shock_event.capitalize()} Shock!")
        else:
            shock_event_placeholder.success("No shock event this time.")
        
        # Increment time and shock probability
        time_elapsed += 1
        shock_probability += 0.001  # Example of increasing shock probability over time
        time.sleep(0.1)

    # After the simulation loop, calculate achievements
    achievement1_progress = min(100, (health_data[-1]/80)*100) if health_data else 0
    achievement2_progress = min(100, (consecutive_enjoyment/5)*100) if enjoyment_data else 0

    # Display simulation results
    st.subheader("Simulation Results")
    data = pd.DataFrame({"Time": range(max_time), "Health": health_data, "Enjoyment": enjoyment_data})
    chart = alt.Chart(data).transform_fold(["Health", "Enjoyment"]).mark_line().encode(
        x="Time:Q",
        y=alt.Y("value:Q", title="Level"),
        color="key:N"
    ).properties(width=600, height=400)
    st.altair_chart(chart)

    # Provide an option to reset the simulation
    if st.button("Reset Simulation"):
        st.experimental_rerun()

    # Add gamification elements (modified according to instructions)
    st.sidebar.header("Achievements")

    # Example of visual progress bars for achievements
    st.sidebar.text("Reached 80% health level")
    st.sidebar.progress(achievement1_progress)

    st.sidebar.text("Maintained enjoyment above 60% for 5 consecutive time steps")
    st.sidebar.progress(achievement2_progress)

    st.sidebar.header("Progress Tracker")
    st.sidebar.progress(70)

# Add tooltips for key concepts
st.markdown("""
<style>
.tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted black;
}

.tooltip .tooltiptext {
    visibility: hidden;
    width: 200px;
    background-color: black;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 5px;
    position: absolute;
    z-index: 1;
    bottom: 100%;
    left: 50%;
    margin-left: -100px;
}

.tooltip:hover .tooltiptext {
    visibility: visible;
}
</style>

<div class="tooltip">Health Shocks
    <span class="tooltiptext">Random events that negatively impact health levels.</span>
</div> | 
<div class="tooltip">Health Level
    <span class="tooltiptext">Represents the participant's current health status.</span>
</div> | 
<div class="tooltip">Enjoyment Level
    <span class="tooltiptext">Represents the participant's current enjoyment status.</span>
</div>
""", unsafe_allow_html=True)
def generate_tank_html(shock_probability, max_balls=10):
    balls_count = int(shock_probability * max_balls)
    tank_html = '<div style="border: 2px solid #333; height: 100px; width: 50px; padding: 5px;">'
    for _ in range(balls_count):
        tank_html += '<div style="background-color: red; height: 8px; width: 8px; border-radius: 50%; margin: 2px;"></div>'
    for _ in range(max_balls - balls_count):
        tank_html += '<div style="background-color: green; height: 8px; width: 8px; border-radius: 50%; margin: 2px;"></div>'
    tank_html += '</div>'
    return tank_html

# Inside the "Run Simulation" button block, after updating the shock probability
shock_probability_display = st.empty()  # Placeholder for the tank visualization

# Update the visualization with the current shock probability
shock_probability_display.markdown(generate_tank_html(shock_probability), unsafe_allow_html=True)