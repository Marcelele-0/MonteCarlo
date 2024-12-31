import numpy as np

def simulate_broadcast(n, p):
    rounds = 0
    received = np.zeros(n, dtype=bool)
    while not np.all(received):
        rounds += 1
        received |= np.random.rand(n) < p
    return rounds
