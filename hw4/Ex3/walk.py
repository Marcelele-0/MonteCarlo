import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import arcsine

def random_walk(n_steps):
    steps = np.random.choice([-1, 1], size=n_steps)  # Losowe kroki -1 lub 1
    position = np.cumsum(steps)  # Sumujemy kroki, aby uzyskać trajektorię
    return position

def compute_fraction_above_ox(n_steps, n_simulations):
    fractions = []
    
    for _ in range(n_simulations):
        walk = random_walk(n_steps)
        d_values = (walk > 0) | (np.concatenate(([0], walk[:-1])) > 0)  # Warunek Dn
        fractions.append(np.sum(d_values) / n_steps)  # PN = LN / N
    
    return np.array(fractions)

def plot_histograms_side_by_side(fractions_list, N_values, bins=20):
    fig, axes = plt.subplots(1, len(N_values), figsize=(15, 5))
    
    for ax, fractions, N in zip(axes, fractions_list, N_values):
        ax.hist(fractions, bins=bins, density=True, alpha=0.7, color='b', edgecolor='black', label="Empiryczny histogram")
        
        # Dodanie teoretycznej gęstości rozkładu arcusa sinusa
        x = np.linspace(0, 1, 100)
        y = arcsine.pdf(x)
        ax.plot(x, y, 'r-', lw=2, label="Rozkład arcusa sinusa")
        
        ax.set_xlabel("Frakcja czasu nad osią OX")
        ax.set_ylabel("Estymowana gęstość prawdopodobieństwa")
        ax.set_title(f"Histogram dla N = {N}")
        ax.legend()
    
    plt.tight_layout()
    plt.show()

# Parametry eksperymentu
N_values = [100, 1000, 10000]  # Liczba kroków
k = 5000  # Liczba realizacji

fractions_list = []
for N in N_values:
    print(f"Eksperyment dla N = {N}")
    fractions = compute_fraction_above_ox(N, k)
    fractions_list.append(fractions)

plot_histograms_side_by_side(fractions_list, N_values)
