import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

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

# Simulated shock probabilities (for demonstration, replace with dynamic values from your model)
shock_probabilities = {
    "No Shock": 0.7,  # 70% probability
    "Small Shock": 0.2,  # 20% probability
    "Large Shock": 0.08,  # 8% probability
    "Death": 0.02  # 2% probability
}

# Display shock probabilities
st.subheader("Shock Probabilities")
for shock_type, probability in shock_probabilities.items():
    st.metric(label=shock_type, value=f"{probability * 100}%")

# Visualizing shock probabilities
st.subheader("Shock Probability Distribution")

# Create a bar chart for shock probabilities
fig, ax = plt.subplots()
ax.bar(shock_probabilities.keys(), shock_probabilities.values(), color=['green', 'yellow', 'orange', 'red'])
ax.set_ylabel('Probability')
ax.set_title('Shock Probability Distribution')

# Display the chart in Streamlit
st.pyplot(fig)

# Integration with C++ dynamic program
# This is where you would call your C++ program or API to get the updated health, enjoyment, and shock event based on the user's decision.
# For example:
# health, enjoyment, shock_event = cpp_simulation.update(decision)

# Displaying the health decline curve and shock probability indicator would require additional logic and visualization tools, potentially integrating with the C++ model's output.
