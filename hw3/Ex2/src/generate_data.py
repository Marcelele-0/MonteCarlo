import random

def generate_random_permutation(n):
    A = list(range(1, n + 1))
    random.shuffle(A)
    return A
