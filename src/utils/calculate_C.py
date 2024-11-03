import numpy as np
import sympy as sp
from multiprocessing import Pool

def calculate_C(n, function_config, M, a, b):
    """Calculate the value of C for a given n, function, and range."""
    if function_config['key'] == 'Pi':
        # Calculate the approximation of Pi
        count_inside_circle = 0
        for _ in range(n):
            x_value = np.random.uniform(-1, 1)
            y_value = np.random.uniform(-1, 1)
            if x_value**2 + y_value**2 <= 1:
                count_inside_circle += 1
        # Approximate Pi based on the ratio of points inside the circle to all points
        pi_approximation = 4 * (count_inside_circle / n)
        return pi_approximation
    else:
        # Standard calculations for other functions
        C = 0
        x = sp.symbols('x')
        function = sp.sympify(function_config['fn'])

        for _ in range(n):
            x_value = np.random.uniform(a, b)
            y_value = np.random.uniform(0, M)
            func_value = function.subs(x, x_value)
            if y_value < func_value:
                C += 1

        return C  # Return the value of C for this n

def calculate_C_list(function_config, M, k, n_values):
    """Calculate a list of C values for different n with k repetitions."""
    a = function_config['a']
    b = function_config['b']
    results = []

    # Prepare for parallel calculation of C values
    with Pool() as pool:
        # Parallel calculation of C for n_values
        for n in n_values:
            counts = pool.starmap(calculate_C, [(n, function_config, M, a, b) for _ in range(k)])
            results.extend(counts)

    return results  # Return the list of C values or Pi approximations for k repetitions
