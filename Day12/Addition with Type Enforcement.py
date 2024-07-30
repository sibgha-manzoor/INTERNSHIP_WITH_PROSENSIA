def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise Exception("Both inputs must be numbers")
    return a + b

print(add_numbers(5, 6))
print(add_numbers(1, "a"))