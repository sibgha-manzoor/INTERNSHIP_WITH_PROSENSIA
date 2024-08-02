def evaluate_polynomial(coefficients, x):
    if not coefficients:
        raise ValueError("The coefficients list cannot be empty")
    
    result = 0
    
    degree = len(coefficients) - 1
    
    for i, coef in enumerate(coefficients):
        if coef != 0: 
            result += coef * (x ** (degree - i))
    
    return result

coefficients_linear = [2, 3]  
coefficients_quadratic = [1, 0, -4]  
coefficients_cubic = [1, -3, 0, 2] 

x_value = 2

print("Linear polynomial evaluation:", evaluate_polynomial(coefficients_linear, x_value))  
print("Quadratic polynomial evaluation:", evaluate_polynomial(coefficients_quadratic, x_value)) 
print("Cubic polynomial evaluation:", evaluate_polynomial(coefficients_cubic, x_value))  