def complex_operations(c1, c2):
    if not (isinstance(c1, tuple) and isinstance(c2, tuple)):
        raise TypeError("Inputs must be tuples")
    if not (len(c1) == 2 and len(c2) == 2):
        raise ValueError("Tuples must be of length 2")
    
    try:
        a, b = c1
        c, d = c2

        if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(d, (int, float))):
            raise TypeError("Tuple elements must be integers or floats")
        
        add_real = a + c
        add_imag = b + d

        sub_real = a - c
        sub_imag = b - d

        mul_real = a * c - b * d
        mul_imag = a * d + b * c

        if c == 0 and d == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number")
        denominator = c * c + d * d
        div_real = (a * c + b * d) / denominator
        div_imag = (b * c - a * d) / denominator

        return {
            'addition': (add_real, add_imag),
            'subtraction': (sub_real, sub_imag),
            'multiplication': (mul_real, mul_imag),
            'division': (div_real, div_imag)
        }

    except ZeroDivisionError as e:
        return str(e)
    except TypeError as e:
        return str(e)
    except ValueError as e:
        return str(e)

c1 = (1, 2)
c2 = (3, 4)

results = complex_operations(c1, c2)
print("Addition:", results['addition'])
print("Subtraction:", results['subtraction'])
print("Multiplication:", results['multiplication'])
print("Division:", results['division'])