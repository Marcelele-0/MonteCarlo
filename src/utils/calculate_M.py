import numpy as np
import sympy as sp

def calculate_M(function_config):
    """
    Calculate the maximum value (M) of a given function over a specified interval.
    
    Parameters:
    function_config (dict): Configuration dictionary containing:
        - 'a' (float): Lower bound of the interval.
        - 'b' (float): Upper bound of the interval.
        - 'fn' (str): The function as a string.
    
    Returns:
    float: Maximum value of the function in the interval [a, b].
    """
    a, b = function_config['a'], function_config['b']
    x = sp.symbols('x')
    function = sp.sympify(function_config['fn'])
    x_vals = np.linspace(a, b, 100)
    y_vals = [float(function.subs(x, val).evalf()) for val in x_vals]
    M = max(y_vals)
    return M