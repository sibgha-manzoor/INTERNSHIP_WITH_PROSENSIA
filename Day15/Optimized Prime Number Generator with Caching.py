def prime_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  
    
    cached_primes = []
    
    for number in range(2, limit + 1):
        if is_prime[number]:
            cached_primes.append(number)
            yield number
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False
    
    def get_cached_primes():
        return cached_primes

limit = 50
print(f"Prime numbers up to {limit}:")
for prime in prime_sieve(limit):
    print(prime, end=" ")