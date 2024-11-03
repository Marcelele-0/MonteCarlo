import numpy as np
import sympy as sp

def calculate_M(function_config):
    """Calculate the maximum value of the function in the given range."""
    a = function_config['a']
    b = function_config['b']
    expression = function_config['fn']

    # Define the symbol x for sympy
    x = sp.symbols('x')

    # Convert the expression to sympy form
    function = sp.sympify(expression)

    # Calculate function values in the given range
    x_vals = np.linspace(a, b, 100)
    y_vals = [function.subs(x, val) for val in x_vals]

    # Find the maximum among the function values
    M = max(y_vals)
    
    return M