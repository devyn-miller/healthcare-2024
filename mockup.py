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
def update_values(health_time, enjoyment_time):
    health = initial_health + health_time - shock_impact * np.random.choice([0, 1], p=[1-shock_probability, shock_probability])
    enjoyment = initial_enjoyment + enjoyment_time
    return health, enjoyment

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

# Create a button to run the simulation
if st.button("Run Simulation"):
    # Initialize variables for tracking progress
    health = initial_health
    enjoyment = initial_enjoyment
    time_elapsed = 0
    health_data = []
    enjoyment_data = []

    # Run the simulation
    while time_elapsed < max_time:
        # Update health and enjoyment based on time allocation
        health, enjoyment = update_values(health_time, enjoyment_time)
        
        # Store data for plotting
        health_data.append(health)
        enjoyment_data.append(enjoyment)
        
        # Update health and enjoyment bars
        health_bar.progress(health)
        enjoyment_bar.progress(enjoyment)
        
        # Display numerical values
        st.write(f"Health: {health}, Enjoyment: {enjoyment}")
        
        # Increment time
        time_elapsed += 1
        time.sleep(0.1)

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

# Add gamification elements (placeholder for demonstration)
st.sidebar.header("Achievements")
st.sidebar.write("- Reached 80% health level")
st.sidebar.write("- Maintained enjoyment above 60% for 5 consecutive time steps")

st.sidebar.header("Progress Tracker")
st.sidebar.progress(70)