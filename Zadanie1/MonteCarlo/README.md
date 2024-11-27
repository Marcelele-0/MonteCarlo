# Monte Carlo Integration Project

## Project Overview

This project aims to approximate integrals using the Monte Carlo method. It includes Python code to perform simulations and generate visualizations of the results. The project is organized to facilitate easy configuration, environment setup, and execution of the simulations. 

## Requirements

- Conda package manager (e.g., via [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html))

## Installation

To set up the project environment and install all necessary dependencies:

1. Clone the repository:
   
    ```bash
    git clone https://github.com/Marcelele-0/MonteCarlo 
    ```

2. Navigate to the project directory:

    ```bash
    cd MonteCarlo
    ```

3. Create and activate the Conda environment:
   
    ```bash
    conda env create -f environment.yaml
    conda activate MonteCarlo
    ```

## Configuration

The `config.yml` file allows for fine-tuning of the Monte Carlo simulation parameters. Here is a breakdown of the configurable options:

- **`n_max`**: The maximum number of iterations the simulation will perform.
- **`n_step`**: The incremental step size for each simulation iteration, allowing for a systematic increase in iterations up to `n_max`.

- **`k_1`** and **`k_2`**: Constants used in the simulation calculations. These values influence how the results are scaled or modified depending on the functions used.

- **`functions`**: A list of functions with specific parameters to evaluate. Each function entry contains:
    - **`key`**: A unique identifier for each function.
    - **`a`** and **`b`**: The lower and upper bounds of the integral for the function.
    - **`fn`**: The function expression in terms of `x`, which will be evaluated over the range `[a, b]`.
    - **`exac_value`**: The expected value of the integral, used to compare the simulation results with the exact solution.

- Adjust these settings in config.yml to modify the behavior of the simulation.



## Contact
    For any questions or issues, contact me at:
    279704@student.pwr.edu.pl