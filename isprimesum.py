"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number
"""

# This is first Approach and this take too mung long time.

def isPrime(A):
    l = [2, 3]
    li = []
    for num in range(2, A + 1):
        i = 0
        for i in range(2, int(num//2)+1):
            if (num % i == 0):
                i = num
                break

        # If the number is prime then print it.
        if(i != num):
            l.append(num)


    for i in l:
        for j in l:
            if i+j==A:
                li.append(i)
                li.append(j)

    return A-max(li), max(li)



# This is the second Approach and takes too less time than first Approach

import math


def isPrime(A):
    l = [2, 3]
    li = []
    for num in range(2, A + 1):
        i = 0
        for i in range(2, int(math.sqrt(A))+1):
            if (num % i == 0):
                i = num
                break

        # If the number is prime then print it.
        if(i != num):
            l.append(num)


    for i in l:
        for j in l:
            if i+j==A:
                li.append(i)
                li.append(j)

    return A-max(li), max(li)



# This is third Approach and this take also much time

def isPrime(A):
    def prime(a):
        if a==1:
            return False
        for i in range(2,  int(math.sqrt(a))+1):
            if a%i==0:
                return False
        return True

    l = []
    for i in range(1, A):
        if i>4:
            if i%2!=0 or i%3!=0:
                if prime(i):
                    l.append(i)
        else:
            if prime(i):
                l.append(i)

    li = []
    for i in l:
        for j in l:
            if i+j==A:
                li.append(i)
                li.append(j)

    return A-max(li), max(li)



# This is forth Approach

def isPrime(A):
    def prime(a):
        if a==1:
            return False
        for i in range(2,  int(math.sqrt(a))+1):
            if a%i==0:
                return False
        return True

    l = []
    for i in range(1, A):
        if i>4:
            if i%2!=0 or i%3!=0:
                if prime(i):
                    l.append(i)
        else:
            if prime(i):
                l.append(i)

    
    li = []
    for i in l:
        for j in l:
            if i+j==A:
                li.append(i)
                li.append(j)

    return A-max(li), max(li)



# This is fifth Approach and this take little bit less time than upper approach
def isPrime(n):
    l = []
    k = []
    for i in range(2, n+1):
        if i not in k:
            l.append(i)
            for j in range(i*i, n+1, i):
                k.append(j)

    # print(l)
    for i in l[::-1]:
        d = n-i
        if d in l:
            return d, i



# THis is sixth Approach and takes much less time but this is take little bit high memory

def isPrime(n):
    limitn = n+1
    not_prime = set()
    l = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        l.append(i)

    
    for i in l[::-1]:
        d = n-i
        if d in l:
            return d, i





# This is seventh Approach and this take too much less time and this is not memory extensive
# and this file best Approach

def isPrime(n):
    limitn = n+1
    not_prime = [False] * limitn
    l = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        l.append(i)

    
    for i in l[::-1]:
        d = n-i
        if d in l:
            return d, i


print(isPrime(16777214))