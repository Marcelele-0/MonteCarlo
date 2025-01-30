import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def simulate_random_walk(N, num_simulations=10000):
    steps = np.random.choice([-1, 1], size=(num_simulations, N))  # Losowe kroki
    return steps.cumsum(axis=1)[:, -1]  # Sumujemy i bierzemy ostatni krok

def plot_empirical_vs_normal(N_values, num_simulations=10000):
    rows = (len(N_values) + 1) // 2
    fig, axes = plt.subplots(rows, 2, figsize=(16, 5 * rows))
    axes = axes.flatten()
    
    for i, N in enumerate(N_values):
        S_N = simulate_random_walk(N, num_simulations)
        
        # Empirical CDF
        sorted_SN = np.sort(S_N)
        empirical_cdf = np.arange(1, len(sorted_SN) + 1) / len(sorted_SN)
        axes[i].plot(sorted_SN, empirical_cdf, label='Empiryczna CDF')
        
        # Normal CDF
        x = np.linspace(-N, N, 1000)
        axes[i].plot(x, stats.norm.cdf(x, loc=0, scale=np.sqrt(N)), '--', label='Normalna CDF')
        
        axes[i].set_title(f"Porównanie dystrybuanty empirycznej i normalnej, N={N}")
        axes[i].set_xlabel("S_N")
        axes[i].set_ylabel("P(S_N ≤ x)")
        axes[i].legend()
    
    # Hide any unused subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
    
    plt.tight_layout()
    plt.savefig('empirical_vs_normal.png')
    plt.show()

# Uruchomienie dla N={5, 10, 15, 20, 25, 30, 100}
N_values = [5, 10, 15, 20, 25, 30, 100]
plot_empirical_vs_normal(N_values)
