def fibonacci(n, depth_limit, current_depth=0):
    if current_depth > depth_limit:
        phi = (1 + 5 ** 0.5) / 2
        return int(phi ** n / 5 ** 0.5 + 0.5)
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1, depth_limit, current_depth + 1) + fibonacci(n-2, depth_limit, current_depth + 1)

n = 10
depth_limit = 20

result = fibonacci(n, depth_limit)
print(f"The {n}-th Fibonacci number is: {result}")