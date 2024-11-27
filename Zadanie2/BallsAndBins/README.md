# Balls and Bins Simulation

This project simulates the process of throwing balls into bins and tracks various metrics.

## Setup

1. Create a virtual environment and activate it:
    ```sh
    conda env create -f env.yaml
    conda activate balls_and_bins_simulation
    ```

2. Run the simulation:
    ```sh
    python src/main.py
    ```

## Configuration

The simulation can be configured using the `config/throwing_config.yaml` file. The following parameters can be adjusted:
- `max_number_of_bins`: Maximum number of bins to simulate.
- `step_size`: Step size for the number of bins.
- `independent_runs`: Number of independent runs per bin count.


