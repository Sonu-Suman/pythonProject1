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