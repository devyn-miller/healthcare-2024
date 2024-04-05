# **Healthcare Software**

## Overview

This project is focused on healthcare analytics, specifically dealing with chronic healthcare data. It includes a comprehensive build system using CMake and Makefile for compiling and linking the project components. The project structure includes configuration readers, modulators, and probability calculators for healthcare data analysis.

## Building the Project

### Prerequisites
- CMake
- GNU Make
- Python 3
- Boost library

### Compilation

To compile the project, clone and then follow these steps:

1. Create a build directory and navigate into it:
    ```shell
    mkdir build && cd build
    ```
2. Run CMake to configure the project:
    ```shell
    cmake ..
    ```
3. Build the project using Make:
    ```shell
    make
    ```

## Running Tests

The project includes unit tests implemented using GoogleTest. To run the tests, execute the following command after building the project:

```shell
./bin/tests_main
```

## Configuration and Execution

The project uses JSON configuration files to set up various parameters for the analysis. A script is provided to run configurations through the built executable and process the output:

```bash
#!/bin/bash
...
done
```

This script processes all JSON configuration files located in the configs directory, runs the analysis, and moves the results to the output directory.

## Project Structure

The project is organized into several key directories:

- `src/`: Contains the source code for the project, including configuration readers and healthcare models.
- `test/`: Contains the unit tests for the project components.
- `configs/`: Contains JSON configuration files for running the project.
- `output/`: Destination directory for analysis results and processed data.

## Key Components

- **Configuration Readers:** Parse JSON configuration files to set up the analysis parameters.
- **Healthcare Modulators:** Implement various healthcare models for the analysis.
- **Probability Calculators:** Calculate probabilities based on healthcare data.


# How DP Works in This Project

1. **Decision Cache:**
- Decision cache to store the results of subproblems.
- Avoids recalculating the results of previously solved subproblems, significantly improving efficiency.
- Utilized for efficient tracking and retrieval of decision outcomes across stages.
   
3. **Storage Mechanism:**
- Storage mechanism to keep track of optimal decisions and their outcomes at different stages of a person's health state.
- Help w tracing back to optimal path after the computation is complete.
   
5. **Optimization Process:**
- At each stage, DP algorithm evaluates all possible decisions based on the current state, considering the impact of each decision on future health outcomes and costs.
- It then selects the decision that maximizes the overall benefit or minimizes the cost over the person's lifetime.
   
7. **Parallel Processing:** OpenMP for parallel processing to speed up the DP computation (handle the computation of multiple stages and scenarios concurrently).
   
8. **Configuration-Driven:** The DP process is highly configurable, allowing users to define various parameters and models through JSON configuration files.
- enables the analysis of different scenarios and healthcare policies.

## Key Components

- **Decision Cache:** Stores the results of subproblems for efficient retrieval.
  
- **Storage:** Keeps track of optimal decisions and outcomes at different health states.
  
- **Configuration:** Allows for the customization of the DP process through JSON files.

## Example Usage

The DP process is initiated by calling the `RunOptimization` function, which takes a configuration object and output directory as arguments. This function orchestrates the optimization process, utilizing the decision cache and storage to compute and store the optimal healthcare decisions.

```
void RunOptimization(std::unique_ptr<const Configuration> config,
                     std::string out_dir, std::string basename);
```


## Stochastic Aspect

1. **Health Shocks:** The model simulates random health shocks that can affect an individual's health state. These shocks are represented probabilistically, reflecting the uncertain nature of health outcomes.

2. **Decision Results:** For each possible decision, the model calculates outcomes considering both the base case and the potential health shocks. This dual consideration enables the evaluation of decisions under uncertainty.

3. **Probability Calculations:** The project uses probability models to estimate the likelihood of different health shocks and their impacts. These models are configurable and can be tailored to specific scenarios or populations.

## Discrete Stages

The optimization process is structured around discrete stages, each representing a period in an individual's life. At each stage, the model evaluates the possible decisions and their outcomes, considering both the current state and the stochastic nature of future states.

1. **Age as a Stage:** Each stage corresponds to an age of the individual, allowing for age-specific decision-making and outcome evaluation.

2. **Transition Between Stages:** The model calculates transitions between stages based on the decisions made and the health shocks experienced. This includes updates to health status, financial resources, and other relevant state variables.

3. **Optimal Path Identification:** After evaluating all stages, the model identifies the optimal path of decisions that maximizes the individual's utility or minimizes costs over their lifetime.
