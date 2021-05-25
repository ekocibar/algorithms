'''GET PRIMES

Get all prime numbers from 1 to n.
'''
def primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for i in range(3,int(n**0.5)+1, 2):
        for j in range(3,(n//i)+1,2):
            sieve[(i*j)]=False

    return [2]+[i for i in range(3,n,2) if sieve[i]]
