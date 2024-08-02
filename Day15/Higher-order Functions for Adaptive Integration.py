def adaptive_quadrature(f, a, b, tol=1e-6, max_depth=20, depth=0):
    def trapezoidal_rule(f, a, b):
        return (b - a) * (f(a) + f(b)) / 2
    
    def simpsons_rule(f, a, b):
        c = (a + b) / 2
        return (b - a) * (f(a) + 4 * f(c) + f(b)) / 6

    c = (a + b) / 2
    integral_trap = trapezoidal_rule(f, a, b)
    integral_simp = simpsons_rule(f, a, b)
    
    if depth >= max_depth or abs(integral_simp - integral_trap) < 15 * tol:
        return integral_simp
    
    left_integral = adaptive_quadrature(f, a, c, tol / 2, max_depth, depth + 1)
    right_integral = adaptive_quadrature(f, c, b, tol / 2, max_depth, depth + 1)
    
    return left_integral + right_integral

import math

def f(x):
    return math.sin(x)

a = 0
b = math.pi
tolerance = 1e-6

result = adaptive_quadrature(f, a, b, tol=tolerance)
print(f"The integral of sin(x) from 0 to pi is approximately: {result}")