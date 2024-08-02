def fibonacci(n, cache=None, max_cache_size=1000):
    if cache is None:
        cache = {0: 0, 1: 1}
    
    if len(cache) > max_cache_size:
        return fibonacci_iterative(n)
    
    if n in cache:
        return cache[n]
    
    if n == 0:
        cache[0] = 0
    elif n == 1:
        cache[1] = 1
    else:
        cache[n] = fibonacci(n-1, cache, max_cache_size) + fibonacci(n-2, cache, max_cache_size)
    
    return cache[n]

def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Example usage
n = 50
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")