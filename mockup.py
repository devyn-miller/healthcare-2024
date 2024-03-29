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

# Update the stick figure representation to use SVG for colored figures
def create_colored_svg_stick_figure_representation(shock_probabilities, total_figures=100):
    # Define SVG template for a stick figure with a placeholder for color
    svg_template = """<svg height="20" width="10" version="1.1" xmlns="http://www.w3.org/2000/svg">
                          <line x1="5" y1="0" x2="5" y2="7" style="stroke:{color};stroke-width:2" />
                          <circle cx="5" cy="3" r="3" style="fill:{color};stroke:none" />
                          <line x1="5" y1="10" x2="5" y2="15" style="stroke:{color};stroke-width:2" />
                          <line x1="2" y1="12" x2="8" y2="12" style="stroke:{color};stroke-width:2" />
                          <line x1="5" y1="15" x2="2" y2="20" style="stroke:{color};stroke-width:2" />
                          <line x1="5" y1="15" x2="8" y2="20" style="stroke:{color};stroke-width:2" />
                      </svg>"""
    # Adjusted colors for better visibility and to accommodate red-green color blindness
    colors = {
        "No Shock": "#808080",  # Gray
        "Small Shock": "#0000FF",  # Blue
        "Large Shock": "#FFA500",  # Orange
        "Death": "#D22B2B"  # Red
    }
    stick_figure_representation = {}
    for shock_type, probability in shock_probabilities.items():
        num_figures = int(probability * total_figures)
        color = colors.get(shock_type, "#000000")  # Default to black if shock type is not found
        # Generate SVG string with colored stick figures
        figures_svg = ''.join([svg_template.format(color=color) for _ in range(num_figures)])
        stick_figure_representation[shock_type] = figures_svg
    return stick_figure_representation

# Calculate colored SVG stick figure representations for shock probabilities
colored_svg_stick_figure_representations = create_colored_svg_stick_figure_representation(shock_probabilities)

# Display colored SVG stick figures for each shock probability category using HTML
st.markdown("<style>.svg-stick-figure { font-size: 24px; }</style>", unsafe_allow_html=True)
st.subheader("Colored SVG Stick Figure Probability Representation")
for shock_type, figures_svg in colored_svg_stick_figure_representations.items():
    st.markdown(f"**{shock_type}:** <div class='svg-stick-figure'>{figures_svg}</div>", unsafe_allow_html=True)

# Legend for colored SVG stick figure representation
st.markdown("""
    <div class='svg-stick-figure-legend' style='font-size: 24px;'>
        <div><svg height="20" width="10"><circle cx="5" cy="3" r="3" style="fill:#808080;stroke:none" /></svg> No Shock (Gray)</div>
        <div><svg height="20" width="10"><circle cx="5" cy="3" r="3" style="fill:#0000FF;stroke:none" /></svg> Small Shock (Blue)</div>
        <div><svg height="20" width="10"><circle cx="5" cy="3" r="3" style="fill:#FFA500;stroke:none" /></svg> Large Shock (Orange)</div>
        <div><svg height="20" width="10"><circle cx="5" cy="3" r="3" style="fill:#D22B2B;stroke:none" /></svg> Death (Red)</div>
    </div>
""", unsafe_allow_html=True)

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
    feedback_message = "You did not experience a shock event today."
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
