import numpy as np

def approximate_pi(n):
    """
    Estimate the value of Pi using the Monte Carlo method.
    
    Parameters:
    n (int): Number of random points to generate.
    
    Returns:
    float: Estimated value of Pi.
    """
    count_inside_circle = 0
    for _ in range(n):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            count_inside_circle += 1
    return (count_inside_circle / n) * 4