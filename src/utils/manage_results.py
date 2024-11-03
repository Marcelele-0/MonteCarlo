import matplotlib.pyplot as plt
import numpy as np
import os

def visualize_results(integral_results_k1, integral_mean_k1, integral_results_k2, integral_mean_k2, function, save_path, k1, k2):
    n_values = list(integral_results_k1.keys())

    # Creating subplots for two different k values
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Plot for k1
    results_matrix_k1 = np.array(list(integral_results_k1.values()))
    for i in range(results_matrix_k1.shape[1]):
        axes[0].scatter(n_values, results_matrix_k1[:, i], color='blue', label='Individual results' if i == 0 else "")
    mean_values_k1 = list(integral_mean_k1.values())
    axes[0].scatter(n_values, mean_values_k1, color='red', label='Mean')
    exact_value = function.get("exact_value")
    if exact_value is not None:
        axes[0].axhline(y=exact_value, color='green', linestyle='--', label='Exact integral value')
    axes[0].set_title(f'Results for function: {function["key"]} (k = {k1})')
    axes[0].set_xlabel('n')
    axes[0].set_ylabel('Integral value')
    axes[0].legend()
    axes[0].grid()

    # Plot for k2
    results_matrix_k2 = np.array(list(integral_results_k2.values()))
    for i in range(results_matrix_k2.shape[1]):
        axes[1].scatter(n_values, results_matrix_k2[:, i], color='blue', label='Individual results' if i == 0 else "")
    mean_values_k2 = list(integral_mean_k2.values())
    axes[1].scatter(n_values, mean_values_k2, color='red', label='Mean')
    if exact_value is not None:
        axes[1].axhline(y=exact_value, color='green', linestyle='--', label='Exact integral value')
    axes[1].set_title(f'Results for function: {function["key"]} (k = {k2})')
    axes[1].set_xlabel('n')
    axes[1].legend()
    axes[1].grid()

    plt.tight_layout()

    # Saving the plot
    if save_path is not None:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        file_path = os.path.join(save_path, f'visualization_{function["key"]}.png')
        plt.savefig(file_path)
        print(f'Plot saved at: {file_path}')
