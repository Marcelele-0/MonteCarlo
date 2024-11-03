def approximate_integral(C, conf, M, n):
    """Calculate the approximation of the integral based on C, a, b, M, and n."""
    a = conf['a']
    b = conf['b']
    area_rectangle = (b - a) * M
    integral_approximation = (C / n) * area_rectangle
    return integral_approximation