def exponentiation_table(base, max_exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("The base must be a numeric value.")
    if not isinstance(max_exponent, int) or max_exponent < 1:
        raise ValueError("The exponent range must be a positive integer.")

    table = []
    for exponent in range(1, max_exponent + 1):
        result = base ** exponent
        table.append(f"{base}^{exponent} = {result}")

    return table

print(exponentiation_table(2, 5))