import numpy as np
import sympy as sp

# Obliczanie wartości M jako maksimum funkcji w przedziale (stała wartość)
def calculate_M(function_config):
    a, b = function_config['a'], function_config['b']
    x = sp.symbols('x')
    function = sp.sympify(function_config['fn'])
    x_vals = np.linspace(a, b, 100)
    y_vals = [float(function.subs(x, val).evalf()) for val in x_vals]
    M = max(y_vals)
    return M