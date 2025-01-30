import scipy.stats as stats
import numpy as np
import pandas as pd
from tabulate import tabulate

def markov_bound(mu, k):
    return mu / k

def chebyshev_bound(var, a):
    return var / a**2

def exact_probability(n, k):
    return 1 - stats.binom.cdf(k - 1, n, 0.5)

def exact_probability_symmetric(n, a):
    return 2 * (1 - stats.binom.cdf(n//2 + a - 1, n, 0.5))

# Parametry
n_values = [100, 1000, 10000]

data = []
for n in n_values:
    mu = n / 2
    var = n / 4
    k1 = int(1.1 * mu)
    a2 = int(0.1 * mu)
    
    markov_k1 = markov_bound(mu, k1)
    chebyshev_a2 = chebyshev_bound(var, a2)
    exact_k1 = exact_probability(n, k1)
    exact_a2 = exact_probability_symmetric(n, a2)
    
    data.append([n, markov_k1, exact_k1, chebyshev_a2, exact_a2])


columns = ["n", "Markov P(X ≥ 1.1E(X))", "Exact P(X ≥ 1.1E(X))", "Chebyshev P(|X - E(X)| ≥ 0.1E(X))", "Exact P(|X - E(X)| ≥ 0.1E(X))"]
df = pd.DataFrame(data, columns=columns)

# Print the table using tabulate for better formatting
print(tabulate(df, headers='keys', tablefmt='pretty'))
