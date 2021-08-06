# This is finding prime numbers between 1 to N.

# This is first Approach

def primes_sieve(n):
    limitn = n+1
    not_prime = [False] * limitn
    l = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        l.append(i)

    return l 


# THis is Second Approach


def primes_sieve(n):
    limitn = n+1
    not_prime = set()
    l = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        l.append(i)

    return l