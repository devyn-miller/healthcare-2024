---
runme:
  id: 01HT59RDGNTDMD9551NQ0CYP1X
  version: v3
---

# Healthcare Investment Experiment App

This Streamlit application simulates a Healthcare Investment Experiment where users can decide how to allocate their time between health investment and enjoyment investment to optimize their life enjoyment. The app incorporates dynamic elements such as health and enjoyment progress bars, shock event notifications, and visualizations of health curves and shock probabilities.

## Features

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

```pip install streamlit```


2. **Download the App**: Download the `mockup.py` file from this repository to a directory on your local machine.

3. **Run the App**: Navigate to the directory containing `mockup.py` in your terminal or command prompt. Run the app by executing:

```streamlit run mockup.py```


This command will start the Streamlit server, and your default web browser should automatically open to the app's URL (typically `http://localhost:8501`).

5. **Interact with the App**: Follow the on-screen instructions to make decisions and interact with the app's features.

## Customizing the App

The app is designed to be easily customizable. You can modify the `mockup.py` file to adjust the probabilities, add new features, or change the visualizations.

**If you have suggestions or want to contribute, please open an issue or pull request in the repository.**