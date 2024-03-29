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
def calculate_shock_probabilities(life_progress, health_investment=50):  # Adjusted for interactivity
    # Adjusted logic for dynamic shock probabilities
    return {
        "No Shock": max(0.7 - life_progress * 0.005 - health_investment * 0.01, 0),
        "Small Shock": 0.2 + life_progress * 0.002 + health_investment * 0.005,
        "Large Shock": 0.08 + life_progress * 0.003 + health_investment * 0.002,
        "Death": 0.02 + life_progress * 0.001 + health_investment * 0.001
    }

# Slider for users to adjust health investment for interactive shock probabilities
health_investment_slider = st.slider("Adjust Health Investment", 0, 100, 50)

# Recalculate shock probabilities based on health investment
shock_probabilities = calculate_shock_probabilities(life_progress, health_investment_slider)

# Visualizing dynamic shock probabilities with a Plotly pie chart
st.subheader("Dynamic Shock Probability Distribution")

# Create a dynamic Plotly pie chart for shock probabilities
fig = go.Figure(data=[go.Pie(labels=list(shock_probabilities.keys()), values=list(shock_probabilities.values()), pull=[0, 0.1, 0.1, 0.2], hole=0.3)])
fig.update_traces(textinfo='percent+label')
fig.update_layout(title_text='Dynamic Shock Probability Distribution')

# Display the dynamic chart in Streamlit using Plotly
st.plotly_chart(fig, use_container_width=True)

# Function to adjust health curve based on parameter
def adjust_health_curve(parameter, age):
    # Placeholder for actual function logic
    adjusted_curve_value = parameter * 100 / (age + 1)  # Simplified example
    return adjusted_curve_value

# Slider for users to adjust the health improvement parameter
parameter_slider = st.slider("Adjust Health Improvement Parameter", 0.0, 1.0, 0.5)

# Display the adjusted health curve
age_array = np.arange(0, 100, 1)  # Example age range
health_curve_values = [adjust_health_curve(parameter_slider, age) for age in age_array]

# Enhanced Health Curve Visualization
health_curve_fig = go.Figure()

# Add a scatter plot for the health curve
health_curve_fig.add_trace(go.Scatter(x=age_array, y=health_curve_values, mode='lines',
                                      line=dict(color='blue', width=3),
                                      name='Health Curve'))

# Add annotations for critical points
health_curve_fig.add_annotation(x=50, y=adjust_health_curve(parameter_slider, 50),
                                text="Critical health investment age",
                                showarrow=True, arrowhead=1)

# Update layout to add more visual appeal
health_curve_fig.update_layout(title_text='Adjusted Health Curve',
                               xaxis_title='Age',
                               yaxis_title='Health Score',
                               plot_bgcolor='white')

st.plotly_chart(health_curve_fig, use_container_width=True)

# Stick Figure Probability Representation
def create_stick_figure_representation(shock_probabilities):
    fig = go.Figure()
    for shock_type, probability in shock_probabilities.items():
        num_figures = int(probability * 100)  # Assuming 100 figures represent 100%
        fig.add_trace(go.Bar(x=[shock_type], y=[num_figures],
                             marker=dict(color='lightblue'),
                             name=f"{shock_type} ({probability:.2%})"))

    fig.update_layout(title_text='Stick Figure Probability Representation',
                      xaxis_title='Shock Type',
                      yaxis_title='Number of Stick Figures',
                      yaxis=dict(range=[0, 100]))  # Assuming 100 is the max number of figures

    return fig

stick_figure_fig = create_stick_figure_representation(shock_probabilities)
st.plotly_chart(stick_figure_fig, use_container_width=True)

# Placeholder for consistency and variance metrics (implementation example)
consistency_placeholder = st.empty()
variance_placeholder = st.empty()

# Example function to calculate consistency and variance (placeholders for actual logic)
def calculate_consistency(user_activity_history):
    return 0.8  # Placeholder value

def calculate_variance(user_activity_history):
    return 0.1  # Placeholder value

# Example user activity history (placeholder)
user_activity_history = [1, 2, 3]  # This would be dynamically updated in a real app

# Calculate and display consistency and variance
consistency = calculate_consistency(user_activity_history)
variance = calculate_variance(user_activity_history)

consistency_placeholder.metric(label="Consistency Score", value=f"{consistency:.2f}")
variance_placeholder.metric(label="Variance Score", value=f"{variance:.2f}")

# Function to provide real-time feedback
def provide_feedback(health, enjoyment, shock_event):
    feedback_message = f"Your current health is {health} and enjoyment is {enjoyment}. "
    if shock_event != "None":
        feedback_message += f"You experienced a shock event: {shock_event}!"
    return feedback_message

# Display real-time feedback
feedback = provide_feedback(health, enjoyment, shock_event)
st.write(feedback)

# Real-Time Feedback with Visual Indicators
if health < 50:
    st.markdown(f"<span style='color:red;'>Your current health is {health}</span>", unsafe_allow_html=True)
else:
    st.markdown(f"<span style='color:green;'>Your current health is {health}</span>", unsafe_allow_html=True)

if enjoyment < 50:
    st.markdown(f"<span style='color:red;'>Your current enjoyment is {enjoyment}</span>", unsafe_allow_html=True)
else:
    st.markdown(f"<span style='color:green;'>Your current enjoyment is {enjoyment}</span>", unsafe_allow_html=True)
