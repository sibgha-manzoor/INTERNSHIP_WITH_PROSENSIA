def swap_variables(a, b):
    a, b = b, a
    return a, b

a = 5
b = 10
print("Before swap: a =", a, ", b =", b)

a, b = swap_variables(a, b)
print("After swap: a =", a, ", b =", b)