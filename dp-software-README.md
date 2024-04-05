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

To compile the project, follow these steps:

1. Clone the repository and navigate to the project directory.
2. Create a build directory and navigate into it:
    ```shell
    mkdir build && cd build
    ```
3. Run CMake to configure the project:
    ```shell
    cmake ..
    ```
4. Build the project using Make:
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
