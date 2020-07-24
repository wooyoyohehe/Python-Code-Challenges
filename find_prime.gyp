factors = set()

def get_factors(n):
    if n < 2:
        return
    if n == 2 or n == 3:
        factors.add(n)
        return factors
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            factors.add(i)
            return get_factors(n/i)
        if i == int(n**0.5):
            factors.add(n)
            return factors
        
get_factors(100)
print factors