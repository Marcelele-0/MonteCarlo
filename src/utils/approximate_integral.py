import numpy as np

def approximate_integral(C, conf, M, n):
    """Calculate the approximation of the integral based on C, a, b, M, and n."""
    a = conf['a']
    b = conf['b']
    area_rectangle = (b - a) * M
    integral_approximation = (C / n) * area_rectangle
    return integral_approximation

def approximate_pi(n):
    count_inside_circle = 0
    for _ in range(n):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            count_inside_circle += 1
    return (count_inside_circle / n) * 4