---
runme:
  id: 01HT59RDGNTDMD9551NQ0CYP1X
  version: v3
---

# Healthcare Investment Experiment App

This Streamlit application simulates a Healthcare Investment Experiment where users can decide how to allocate their time between health investment and enjoyment investment to optimize their life enjoyment. The app incorporates dynamic elements such as health and enjoyment progress bars, shock event notifications, and visualizations of health curves and shock probabilities.

## Features

The `mockup.py` Streamlit app allows users to make daily investment decisions between health and enjoyment, simulates the impact of these decisions along with random health shocks, and visualizes the outcomes. Here's a breakdown of its components and functions:

### Initial Setup and Introduction
- **Streamlit Configuration**: The page is configured with a title and icon.
- **Introduction Section**: Presents the experiment's purpose and mechanics to the user.

### Decision Making
- **Binary Decision**: Users choose between investing in health or enjoyment for the day.

### Simulation Mechanics
- **Health and Enjoyment Tracking**: Initializes placeholders for displaying health and enjoyment progress bars.
- **Daily Simulation**: Simulates the effect of the user's decision on health and enjoyment, including the possibility of a random shock event affecting health.

### Shock Event Handling
- **Shock Event Simulation**: Randomly determines if a shock event occurs each day and updates health accordingly.
- **Shock Event Notification**: Displays a notification about the shock event, if any.

### Gamification and Progress Tracking
- **Achievements**: Displays achievements based on health and enjoyment levels.
- **Life Progress Slider**: Allows users to adjust their life progress, simulating aging.

### Dynamic Shock Probabilities
- **`calculate_shock_probabilities` Function**: Calculates the probabilities of different shock events based on the user's life progress and health investment.
- **Health Investment Slider**: Lets users adjust their health investment level, affecting shock probabilities.
- **Shock Probability Visualization**: Uses a Plotly pie chart to visualize the dynamic shock probabilities.

### Health Curve Adjustment
- **`gompertz_function` Function**: Defines a Gompertz function to model the health curve based on age and health investment.
- **Health Curve Visualization**: Visualizes the adjusted health curve using a Plotly scatter plot, highlighting the critical age for health investment.

### Consistency and Variance Metrics
- **`calculate_consistency` Function**: Calculates the consistency of user activity based on the variance of differences in activity levels.
- **Consistency and Variance Display**: Shows the calculated consistency and variance metrics to the user.

### Real-Time Feedback
- **`provide_feedback` Function**: Generates a feedback message based on the day's events, health, and enjoyment levels.
- **Visual Indicators**: Displays health and enjoyment levels with color-coded visual indicators for immediate feedback.

### SVG Stick Figure Representation
- **`create_colored_svg_stick_figure_representation` Function**: Generates SVG representations of shock probabilities with color coding for better visibility and accessibility.
- **SVG Stick Figure Display**: Shows the SVG stick figures representing shock probabilities and includes a legend for interpretation.



## User-End
- **Decision Making**: Choose daily investments in health or enjoyment.
- **Health and Enjoyment Tracking**: Visual progress bars update based on your decisions.
- **Shock Events**: Randomly occurring events that can negatively impact your health.
- **Dynamic Shock Probabilities**: Visualize how different levels of health investment affect the probability of shock events.
- **Health Curve Adjustment**: See how your health investment decisions affect your health curve over time.
- **Achievements**: Track your progress and achievements through sidebar indicators.
- **Real-Time Feedback**: Receive immediate feedback on your health and enjoyment levels after each decision.
- **Critical Age Explanation**: View a detailed explanation of how the critical age for health investment is determined, helping users make informed decisions.
- **Interactive Explanations**: Look for the `?` icon or hover over certain elements within the app to get detailed explanations and insights. This feature is designed to enhance your understanding of the simulation and its underlying assumptions.

## How to Launch the App Locally

To run the Healthcare Investment Experiment app on your local machine, follow these steps:

1. **Install Streamlit**: Open your terminal or command prompt and install Streamlit using pip:

`pip install streamlit`

(Optionally, install all requirements by running the following command in your terminal: `pip install -r requirements.txt`)

2. **Download the App**: Download the `mockup.py` file from this repository to a directory on your local machine.
3. **Run the App**: Navigate to the directory containing `mockup.py` in your terminal or command prompt. Run the app by executing:

`streamlit run mockup.py`

This command will start the Streamlit server, and your default web browser should automatically open to the app's URL (typically `http://localhost:8501`).

5. **Interact with the App**: Follow the on-screen instructions to make decisions and interact with the app's features.

## Customizing the App

The app is designed to be easily customizable. You can modify the `mockup.py` file to adjust the probabilities, add new features, or change the visualizations.

**If you have suggestions or want to contribute, please open an issue or pull request in the repository.**
