import matplotlib.pyplot as plt
import os

def plot_results(n_values, all_results, p, output_dir):
    plt.figure(figsize=(12, 8))  # Make the plot twice as big
    for i, n in enumerate(n_values):
        # Plot individual data points with smaller blue dots
        plt.scatter([n] * len(all_results[i]), all_results[i], color='blue', s=5, alpha=0.5)
        # Plot the average with a red marker
        plt.scatter(n, sum(all_results[i]) / len(all_results[i]), color='red', s=50, zorder=5)
    
    plt.xlabel('Number of nodes (n)')
    plt.ylabel('Number of rounds (Tn)')
    plt.title(f'Number of rounds needed for p = {p}')
    plt.grid(True)
    
    # Save the plot as a PNG file
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    plt.savefig(os.path.join(output_dir, f'results_p_{p}.png'))
    
    # Show the plot
    plt.show()
