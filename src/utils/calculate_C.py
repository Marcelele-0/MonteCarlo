import numpy as np
import sympy as sp
from multiprocessing import Pool

def calculate_C(n, function_config, M, a, b):
    """Calculate the value of C for a given n, function, and range."""
    C = 0
    x = sp.symbols('x')
    function = sp.sympify(function_config['fn'])

    for _ in range(n):
        x_value = np.random.uniform(a, b)
        y_value = np.random.uniform(0, M)
        func_value = function.subs(x, x_value)

        # Ensure func_value is a numerical value before comparison
        try:
            func_value_numeric = float(func_value.evalf())  # Convert to float
        except Exception as e:
            print(f"Error evaluating function at x={x_value}: {func_value}, Error: {e}")
            continue  # Skip this iteration if evaluation fails

        # Make comparison with the numeric value
        if y_value < func_value_numeric:
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