import matplotlib.pyplot as plt
import numpy as np
import os
from typing import Dict, List


def visualize_results(
    integral_results_k1: Dict[int, List[float]],
    integral_mean_k1: Dict[int, float],
    integral_results_k2: Dict[int, List[float]],
    integral_mean_k2: Dict[int, float],
    function: Dict,
    save_path: str,
    k1: int,
    k2: int,
    colors: dict = {'individual': 'blue', 'mean': 'red', 'exac': '#90EE90'}
):
    """
    Visualize the results of integral approximations for two different k values.

    Parameters:
    integral_results_k1 (Dict[int, List[float]]): Integral results for k1.
    integral_mean_k1 (Dict[int, float]): Mean integral values for k1.
    integral_results_k2 (Dict[int, List[float]]): Integral results for k2.
    integral_mean_k2 (Dict[int, float]): Mean integral values for k2.
    function (Dict): Dictionary containing function details including 'key' and 'exac_value'.
    save_path (str): Path to save the plot.
    k1 (int): First k value.
    k2 (int): Second k value.
    colors (dict): Dictionary specifying colors for individual results, mean, and exact value.
    """
    n_values = list(integral_results_k1.keys())

    # Creating subplots for two different k values (stacked vertically)
    fig, axes = plt.subplots(2, 1, figsize=(15, 18))

    # Plot for k1
    results_matrix_k1 = np.array(list(integral_results_k1.values()))
    for i in range(results_matrix_k1.shape[1]):
        axes[0].scatter(
            n_values, results_matrix_k1[:, i], color=colors['individual'], s=10,
            label='Individual results' if i == 0 else ""
        )
    mean_values_k1 = list(integral_mean_k1.values())
    axes[0].scatter(n_values, mean_values_k1, color=colors['mean'], s=20, label='Mean')
    exac_value = function.get("exac_value")
    if exac_value is not None:
        axes[0].axhline(y=exac_value, color=colors['exac'], linestyle='-', label='Exac integral value')
    axes[0].set_title(f'Results for function: {function["key"]} (k = {k1})')
    axes[0].set_xlabel('n')
    axes[0].set_ylabel('Integral value')
    axes[0].legend()
    axes[0].grid()

    # Plot for k2
    results_matrix_k2 = np.array(list(integral_results_k2.values()))
    for i in range(results_matrix_k2.shape[1]):
        axes[1].scatter(
            n_values, results_matrix_k2[:, i], color=colors['individual'], s=10,
            label='Individual results' if i == 0 else ""
        )
    mean_values_k2 = list(integral_mean_k2.values())
    axes[1].scatter(n_values, mean_values_k2, color=colors['mean'], s=20, label='Mean')
    if exac_value is not None:
        axes[1].axhline(y=exac_value, color=colors['exac'], linestyle='-', label='Exac integral value')
    axes[1].set_title(f'Results for function: {function["key"]} (k = {k2})')
    axes[1].set_xlabel('n')
    axes[1].legend()
    axes[1].grid()

    plt.tight_layout()

    # Saving the plot
    if save_path is not None:
        try:
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            file_path = os.path.join(save_path, f'visualization_{function["key"]}.png')
            plt.savefig(file_path)
            print(f'Plot saved at: {file_path}')
        except Exception as e:
            print(f"Error saving plot: {e}")

    plt.close(fig)  # Close the figure to free up memory


def visualize_results_Pi(
    integral_results_k1: Dict[int, List[float]],
    integral_mean_k1: Dict[int, float],
    integral_results_k2: Dict[int, List[float]],
    integral_mean_k2: Dict[int, float],
    function: Dict,
    save_path: str,
    k1: int,
    k2: int,
    show_plot: bool = False,
    colors: dict = {'individual': 'blue', 'mean': 'red', 'exac': '90EE90'}
):
    """
    Visualize the results of π approximations for two different k values.

    Parameters:
    integral_results_k1 (Dict[int, List[float]]): Integral results for k1.
    integral_mean_k1 (Dict[int, float]): Mean integral values for k1.
    integral_results_k2 (Dict[int, List[float]]): Integral results for k2.
    integral_mean_k2 (Dict[int, float]): Mean integral values for k2.
    function (Dict): Dictionary containing function details including 'key' and 'exac_value'.
    save_path (str): Path to save the plot.
    k1 (int): First k value.
    k2 (int): Second k value.
    show_plot (bool): Whether to display the plot.
    colors (dict): Dictionary specifying colors for individual results, mean, and exact value.
    """
    n_values = list(integral_results_k1.keys())

    # Creating subplots for two different k values (stacked vertically)
    fig, axes = plt.subplots(2, 1, figsize=(15, 18))

    # Plot for k1
    results_matrix_k1 = np.array(list(integral_results_k1.values()))
    for i in range(results_matrix_k1.shape[1]):
        axes[0].scatter(
            n_values, results_matrix_k1[:, i], color=colors['individual'], s=10,
            label='Individual results' if i == 0 else ""
        )
    mean_values_k1 = list(integral_mean_k1.values())
    axes[0].scatter(n_values, mean_values_k1, color=colors['mean'], s=20, label='Mean')
    exac_value = function.get("exac_value")
    if exac_value is not None:
        axes[0].axhline(y=exac_value, color=colors['exac'], linestyle='-', label='Exac value of π')
    axes[0].set_title(f'Approximation of π (k = {k1})')
    axes[0].set_xlabel('Number of points n')
    axes[0].set_ylabel('Approximation of π')
    axes[0].legend()
    axes[0].grid()

    # Plot for k2
    results_matrix_k2 = np.array(list(integral_results_k2.values()))
    for i in range(results_matrix_k2.shape[1]):
        axes[1].scatter(
            n_values, results_matrix_k2[:, i], color=colors['individual'], s=10,
            label='Individual results' if i == 0 else ""
        )
    mean_values_k2 = list(integral_mean_k2.values())
    axes[1].scatter(n_values, mean_values_k2, color=colors['mean'], s=20, label='Mean')
    if exac_value is not None:
        axes[1].axhline(y=exac_value, color=colors['exac'], linestyle='-', label='Exac value of π')
    axes[1].set_title(f'Approximation of π (k = {k2})')
    axes[1].set_xlabel('Number of points n')
    axes[1].legend()
    axes[1].grid()

    plt.tight_layout()

    # Saving the plot
    if save_path is not None:
        try:
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            file_path = os.path.join(save_path, f'visualization_pi.png')
            plt.savefig(file_path)
            print(f'Plot saved at: {file_path}')
        except Exception as e:
            print(f"Error saving plot: {e}")

    if show_plot:
        plt.show()

    plt.close(fig)  # Close the figure to free up memory
