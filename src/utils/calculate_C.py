import numpy as np
import sympy as sp
from multiprocessing import Pool
from joblib import Parallel, delayed

# Zoptymalizowana funkcja obliczająca C dla danego n, wektoryzowana
def calculate_C_vectorized(n, numeric_function, M, a, b):
    x_values = np.random.uniform(a, b, n)
    y_values = np.random.uniform(0, M, n)
    func_values = numeric_function(x_values)
    C = np.sum(y_values < func_values)
    return C

# Równoległe obliczanie wartości C dla n i k
def calculate_C_parallel(n, numeric_function, M, a, b, k):
    return Parallel(n_jobs=-1)(delayed(calculate_C_vectorized)(n, numeric_function, M, a, b) for _ in range(k))

def get_numeric_function(expression):
    x = sp.symbols('x')
    symbolic_function = sp.sympify(expression)
    return sp.lambdify(x, symbolic_function, 'numpy')