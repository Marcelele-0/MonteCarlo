import numpy as np
from .simulation import simulate_broadcast

def run_experiments(n_values, p, k, logger):
    all_results = []
    for n in n_values:
        logger.info(f"Running {k} simulations for n = {n}, p = {p}")
        rounds_needed = [simulate_broadcast(n, p) for _ in range(k)]
        all_results.append(rounds_needed)
    return all_results
