"""This is working less than thousand number."""

import string as s

def isPrime(A):
    assert A>=1, 'Please enter the positive integer.'

    
    if A==1:
            return []
    else:
        m = int(A**(0.5))
        for j in range(2, m+1):
            if A%j==0:
                return isPrime(A-1)
        return [i for i in [A, isPrime(A-1)] if i!=list()]
        # return A, isPrime(A-1)

s = isPrime(500)
def extract(s):
    l = []
    for i in s:
        if type(i) is list:
            l.extend(extract(i))
        else:
            l.append(i)

    return l



print(*extract(s)[::-1])


# This is the second method


def PrimeNumbers(n):
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


print(PrimeNumbers(20000000))


# This is the third methode but slower than two

import math
import time

def isPrime(A):
    l = [2, 3]
    for num in range(2, A + 1):
        i = 0
        for i in range(2, int(math.sqrt(A))+1):
            if num % i == 0:
                i = num
                break

        # If the number is prime then print it.
        if i != num:
            l.append(num)


t1 = time.time()
print(isPrime(200000))
t2 = time.time()
print(t2-t1)