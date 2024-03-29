import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Initial setup
st.set_page_config(page_title="Healthcare Investment Experiment", page_icon=":hospital:")

# Introduction
st.title("Healthcare Investment Experiment")
st.markdown("""
Welcome to the Healthcare Investment Experiment! In this simulation, you will decide how to allocate your time between health investment and enjoyment investment to optimize your life enjoyment. Your health will naturally decline over time, and you will face random health shocks that can affect your health and enjoyment.
""")

# Binary decision making
decision = st.radio("Choose your investment for today:", ('Health Investment', 'Enjoyment Investment'))

# Placeholder for health and enjoyment bars
health_bar = st.empty()
enjoyment_bar = st.empty()

# Simulate one day in the experiment (this would be part of a loop or triggered by a button in a real experiment)
health, enjoyment = 50, 50  # Initial values
shock_event = "None"  # Placeholder for shock event

# Placeholder for shock event notification
shock_event_placeholder = st.empty()

# Update health and enjoyment based on decision
if decision == 'Health Investment':
    health += np.random.randint(1, 5)  # Simulate health improvement
else:
    enjoyment += np.random.randint(1, 5)  # Simulate enjoyment increase

# Randomly determine if a shock event occurs
if np.random.rand() < 0.1:  # Example probability
    shock_event = "Small Shock"
    health -= np.random.randint(5, 10)

# Update health and enjoyment bars
health_bar.progress(health)
enjoyment_bar.progress(enjoyment)

# Display shock event notification
if shock_event != "None":
    shock_event_placeholder.error(f"Shock Event: {shock_event}!")
else:
    shock_event_placeholder.success("No shock event today.")

# Gamification elements
st.sidebar.header("Achievements")
st.sidebar.markdown("* Survived a day without a shock: 🏅")
st.sidebar.markdown("* Reached 60% health: 🏅" if health >= 60 else "* Reach 60% health: ❌")
st.sidebar.markdown("* Reached 60% enjoyment: 🏅" if enjoyment >= 60 else "* Reach 60% enjoyment: ❌")

# Life Progress Slider
life_progress = st.slider("Life Progress", 0, 100, 50)

# Function to calculate dynamic shock probabilities
def calculate_shock_probabilities(life_progress):
    # This function should contain the logic to calculate shock probabilities
    # based on the life progress. For simplicity, we're using static values here.
    return {
        "No Shock": max(0.7 - life_progress * 0.005, 0),
        "Small Shock": 0.2 + life_progress * 0.002,
        "Large Shock": 0.08 + life_progress * 0.003,
        "Death": 0.02 + life_progress * 0.001
    }

# Calculate dynamic shock probabilities based on life progress
shock_probabilities = calculate_shock_probabilities(life_progress)

# Visualizing dynamic shock probabilities with a Plotly pie chart
st.subheader("Dynamic Shock Probability Distribution")

# Create a dynamic Plotly pie chart for shock probabilities
fig = go.Figure(data=[go.Pie(labels=list(shock_probabilities.keys()), values=list(shock_probabilities.values()), pull=[0, 0.1, 0.1, 0.2], hole=0.3)])
fig.update_traces(textinfo='percent+label')
fig.update_layout(title_text='Dynamic Shock Probability Distribution')

# Display the dynamic chart in Streamlit using Plotly
st.plotly_chart(fig, use_container_width=True)
#