factors = list()

def find_factors(n):
    i=2
    print "n=" + str(n)
    while(i<=n):
        if n%i==0:
            factors.append(i)
            n = n/i
        else: 
            i+=1
    return factors
        
find_factors(100)
print factors