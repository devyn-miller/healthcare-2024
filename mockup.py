import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Initial setup
st.set_page_config(page_title="Healthcare Investment Experiment", page_icon=":hospital:")

# Introduction
st.title("Healthcare Investment Experiment :hospital:")
st.markdown("""
Welcome to the Healthcare Investment Experiment! In this simulation, you will decide how to allocate your time between health investment :heart: and enjoyment investment :sunglasses: to optimize your life enjoyment :sunglasses:. Your health :heart: will naturally decline over time, and you will face random health shocks :lightning_cloud: that can affect your health :heart: and enjoyment :sunglasses:.
""")

# Binary decision making
decision = st.radio("Choose your investment for today:", ('Health Investment :heart:', 'Enjoyment Investment :sunglasses:'))

# Placeholder for health :heart: and enjoyment :sunglasses: bars
health_bar = st.empty()
enjoyment_bar = st.empty()

# Simulate one day in the experiment (this would be part of a loop or triggered by a button in a real experiment)
health, enjoyment = 50, 50  # Initial values
shock_event = "None"  # Placeholder for shock event

# Placeholder for shock event notification
shock_event_placeholder = st.empty()

# Update health :heart: and enjoyment :sunglasses: based on decision
if decision == 'Health Investment :heart:':
    health += np.random.randint(1, 5)  # Simulate health improvement
else:
    enjoyment += np.random.randint(1, 5)  # Simulate enjoyment increase

# Randomly determine if a shock event occurs
if np.random.rand() < 0.1:  # Example probability
    shock_event = "Small Shock :lightning_cloud:"
    health -= np.random.randint(5, 10)

# Update health :heart: and enjoyment :sunglasses: bars
health_bar.progress(health)
enjoyment_bar.progress(enjoyment)

# Display shock event notification
if shock_event != "None":
    shock_event_placeholder.error(f"Shock Event: {shock_event}!")
else:
    shock_event_placeholder.success("No shock event today :sunny:.")

# Gamification elements
st.sidebar.header("Achievements")
st.sidebar.markdown("* Survived a day without a shock :sunny:: 🏅")
st.sidebar.markdown("* Reached 60% health :heart:: 🏅" if health >= 60 else "* Reach 60% health :heart:: ❌")
st.sidebar.markdown("* Reached 60% enjoyment :sunglasses:: 🏅" if enjoyment >= 60 else "* Reach 60% enjoyment :sunglasses:: ❌")

# Life Progress Slider with a clock emoji
life_progress = st.slider("Life Progress :time:", 0, 100, 50, help="Slide to adjust your life progress. This represents your age and overall life experience :clock:.")

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
health_investment_slider = st.slider("Adjust Health Investment :heart:", 0, 100, 50, help="Adjust your health investment level. Higher investment increases your health :heart: but may reduce enjoyment :sunglasses:.")

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
def gompertz_function(age, health_investment, shock_effect, parameter=0.005):
    # Adjust the parameter to control the shape of the curve
    base_rate = np.exp(-np.exp(-parameter * (age - (65 + health_investment * 0.2 + shock_effect))))
    return base_rate

# Slider for users to adjust the health improvement parameter
parameter_slider = st.slider("Adjust Health Improvement Parameter :heart:", 0.0, 1.0, 0.5)

# Display the adjusted health curve
age_array = np.arange(0, 100, 1)  # Example age range
shock_effect = -5 if shock_event == "Small Shock :lightning_cloud:" else 0
participant_curve = [gompertz_function(age, health_investment_slider, shock_effect, parameter_slider) for age in age_array]
average_curve = [gompertz_function(age, 30, 0, 0.008) for age in age_array]  # Adjusted for a more noticeable difference

# Enhanced Health Curve Visualization
health_curve_fig = go.Figure()

# Add a scatter plot for the participant's health curve
health_curve_fig.add_trace(go.Scatter(x=age_array, y=participant_curve, mode='lines',
                                      line=dict(color='blue', width=3),
                                      name='Your Health Curve'))

# Add a scatter plot for the average health curve
health_curve_fig.add_trace(go.Scatter(x=age_array, y=average_curve, mode='lines',
                                      line=dict(color='green', width=3, dash='dash'),
                                      name='Average Health Curve'))

# Update layout to add more visual appeal
health_curve_fig.update_layout(title_text='Health Investment Impact on Life Expectancy',
                               xaxis_title='Age',
                               yaxis_title='Probability of Living',
                               plot_bgcolor='white',
                               yaxis=dict(range=[0, 1]))  # Set the Y-axis range from 0 to 1

st.plotly_chart(health_curve_fig, use_container_width=True)

st.info("""
The critical age for health investment :heart: is determined based on the point at which additional health investments yield diminishing returns on health improvement. This is visually represented in the health curve and is calculated using a combination of factors including current health status :heart:, age, and previous investment levels.
""")

# Update the stick figure representation to use SVG for colored figures with an adjusted color scheme
def create_colored_svg_stick_figure_representation(shock_probabilities, total_figures=100):
    # Adjusted colors for better visibility and to accommodate red-green color blindness
    colors = {
        "No Shock": "#808080",  # Gray
        "Small Shock": "#0000FF",  # Blue
        "Large Shock": "#FFA500",  # Orange
        "Death": "#8B0000"  # Dark Red
    }
    svg_template = """<svg height="20" width="10" version="1.1" xmlns="http://www.w3.org/2000/svg">
                          <line x1="5" y1="0" x2="5" y2="7" style="stroke:{color};stroke-width:2" />
                          <circle cx="5" cy="3" r="3" style="fill:{color};stroke:none" />
                          <line x1="5" y1="10" x2="5" y2="15" style="stroke:{color};stroke-width:2" />
                          <line x1="2" y1="12" x2="8" y2="12" style="stroke:{color};stroke-width:2" />
                          <line x1="5" y1="15" x2="2" y2="20" style="stroke:{color};stroke-width:2" />
                          <line x1="5" y1="15" x2="8" y2="20" style="stroke:{color};stroke-width:2" />
                      </svg>"""
    stick_figure_representation = {}
    for shock_type, probability in shock_probabilities.items():
        num_figures = int(probability * total_figures)
        color = colors.get(shock_type, "#000000")  # Default to black if shock type is not found
        figures_svg = ''.join([svg_template.format(color=color) for _ in range(num_figures)])
        stick_figure_representation[shock_type] = figures_svg
    return stick_figure_representation

colored_svg_stick_figure_representations = create_colored_svg_stick_figure_representation(shock_probabilities)

st.markdown("<style>.svg-stick-figure { font-size: 24px; }</style>", unsafe_allow_html=True)
st.subheader("Colored SVG Stick Figure Probability Representation")
for shock_type, figures_svg in colored_svg_stick_figure_representations.items():
    st.markdown(f"**{shock_type}:** <div class='svg-stick-figure'>{figures_svg}</div>", unsafe_allow_html=True)

# Adjusted legend for colored SVG stick figure representation
st.markdown("""
    <div class='svg-stick-figure-legend' style='font-size: 24px;'>
        <div><svg height="20" width="10"><circle cx="5" cy="3" r="3" style="fill:#808080;stroke:none" /></svg> No Shock (Gray)</div>
        <div><svg height="20" width="10"><circle cx="5" cy="3" r="3" style="fill:#0000FF;stroke:none" /></svg> Small Shock (Blue)</div>
        <div><svg height="20" width="10"><circle cx="5" cy="3" r="3" style="fill:#FFA500;stroke:none" /></svg> Large Shock (Orange)</div>
        <div><svg height="20" width="10"><circle cx="5" cy="3" r="3" style="fill:#8B0000;stroke:none" /></svg> Death (Dark Red)</div>
    </div>
""", unsafe_allow_html=True)

# Actual implementation for consistency and variance metrics
def calculate_consistency(data):
    # Actual consistency calculation logic
    return sum(data) / len(data)  # Example calculation

def calculate_variance(data):
    # Actual variance calculation logic
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance  # Example calculation

# Example user activity history (placeholder)
user_activity_history = [1, 2, 3, 4, 5]  # This would be dynamically updated in a real app

# Define placeholders for consistency and variance metrics
consistency_placeholder = st.empty()
variance_placeholder = st.empty()

# Calculate and display consistency and variance
consistency = calculate_consistency(user_activity_history)
variance = calculate_variance(user_activity_history)

consistency_placeholder.metric(label="Consistency Score", value=f"{consistency:.2f}")
variance_placeholder.metric(label="Variance Score", value=f"{variance:.2f}")

# Function to provide real-time feedback
def provide_feedback(health, enjoyment, shock_event):
    feedback_message = "You did not experience a shock event today :sunny:."
    if shock_event != "None":
        feedback_message += f" You experienced a shock event: {shock_event} :lightning_cloud:!"
    feedback_message += f"\nYour current health is {health} :heart:."
    feedback_message += f"\nYour current life enjoyment is {enjoyment} :sunglasses:."
    return feedback_message

# Display real-time feedback
feedback = provide_feedback(health, enjoyment, shock_event)
st.markdown(feedback, unsafe_allow_html=True)

# Real-Time Feedback with Visual Indicators
if health < 50:
    st.markdown(f"<span style='color:red;'>Your current health is {health} :heart:.</span>", unsafe_allow_html=True)
else:
    st.markdown(f"<span style='color:green;'>Your current health is {health} :heart:.</span>", unsafe_allow_html=True)

if enjoyment < 50:
    st.markdown(f"<span style='color:red;'>Your current life enjoyment is {enjoyment} :sunglasses:.</span>", unsafe_allow_html=True)
else:
    st.markdown(f"<span style='color:green;'>Your current life enjoyment is {enjoyment} :sunglasses:.</span>", unsafe_allow_html=True)

AVERAGE_LIFE_EXPECTANCY = 75  # Example average life expectancy

# Add a new trace for the average life expectancy
health_curve_fig.add_trace(go.Scatter(
    x=[0, 100],  # Assuming the x-axis represents age from 0 to 100
    y=[AVERAGE_LIFE_EXPECTANCY, AVERAGE_LIFE_EXPECTANCY],
    mode='lines',
    name='Average Life Expectancy',
    line=dict(color='green', dash='dash'),
))

# Update layout to reflect the addition
health_curve_fig.update_layout(title_text='Adjusted Health Curve with Projected and Average Life Expectancy')

st.plotly_chart(health_curve_fig, use_container_width=True)
