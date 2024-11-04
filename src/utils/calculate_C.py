import numpy as np
import sympy as sp
from joblib import Parallel, delayed

def calculate_C_vectorized(n, numeric_function, M, a, b):
    """
    Estimate the integral using the Monte Carlo method.
    
    Parameters:
    n (int): Number of random points.
    numeric_function (function): The function to integrate.
    M (float): Maximum value of the function in the interval [a, b].
    a (float): Lower bound of the interval.
    b (float): Upper bound of the interval.
    
    Returns:
    float: Estimated value of the integral.
    """
    x_values = np.random.uniform(a, b, n)
    y_values = np.random.uniform(0, M, n)
    func_values = numeric_function(x_values)
    C = np.sum(y_values < func_values)
    # Convert the number of points under the curve to an integral approximation
    integral_estimate = (b - a) * M * C / n
    return integral_estimate

def calculate_integrals_parallel(n, numeric_function, M, a, b, k):
    """
    Calculate the integral in parallel for given n and k.
    
    Parameters:
    n (int): Number of random points.
    numeric_function (function): The function to integrate.
    M (float): Maximum value of the function in the interval [a, b].
    a (float): Lower bound of the interval.
    b (float): Upper bound of the interval.
    k (int): Number of parallel computations.
    
    Returns:
    list: List of estimated integral values.
    """
    return Parallel(n_jobs=-1)(
        delayed(calculate_C_vectorized)(n, numeric_function, M, a, b) for _ in range(k)
    )

def get_numeric_function(expression):
    """
    Convert a symbolic expression to a numeric function.
    
    Parameters:
    expression (str): The symbolic expression as a string.
    
    Returns:
    function: The numeric function.
    """
    x = sp.symbols('x')
    symbolic_function = sp.sympify(expression)
    return sp.lambdify(x, symbolic_function, 'numpy')