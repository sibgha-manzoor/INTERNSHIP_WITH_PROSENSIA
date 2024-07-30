def divide_and_round(numerator, denominator, precision):
    if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
        raise TypeError("Both numerator and denominator must be numeric values.")
    if not isinstance(precision, int) or precision < 0:
        raise ValueError("Precision must be a non-negative integer.")
    
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    
    result = numerator / denominator
    return round(result, precision)

print(divide_and_round(5, 2, 2))
print(divide_and_round(5, 0, 2))