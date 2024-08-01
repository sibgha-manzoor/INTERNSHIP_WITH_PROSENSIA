def prime_factors_and_product(n):
    def prime_factors(num):
        factors = []
        while num % 2 == 0:
            factors.append(2)
            num //= 2
        factor = 3
        while factor * factor <= num:
            while num % factor == 0:
                factors.append(factor)
                num //= factor
            factor += 2
        if num > 2:
            factors.append(num)
        return factors
    
    if n < 2:
        return [], 1  
    
    factors = prime_factors(n)
    product = 1
    for factor in factors:
        product *= factor
    
    return factors, product

number = 60
factors, product = prime_factors_and_product(number)
print(f"Prime factors of {number}: {factors}")
print(f"Product of prime factors: {product}")