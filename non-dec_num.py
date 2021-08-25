# Number of n-digits non-decreasing integers

"""
Given an integer n > 0, which denotes the number of digits, 
the task to find the total number of n-digit positive integers which are non-decreasing in nature. 
A non-decreasing integer is one in which all the digits from left to right are in non-decreasing form. ex: 1234, 1135, ..etc. 
Note: Leading zeros also count in non-decreasing integers such as 0000, 0001, 0023, etc are 
also non-decreasing integers of 4-digits. 
"""

# This is the solution

def count(n):
    c = []
    k = []
    if n==1:
        total = 10

    if n>1:
        total = 10
        for i in range(int('9'*n)+1):
            c.clear()
            k.clear()
            if len(str(i))>1:
                for j in str(i):
                    c.append(int(j))

                for m in str(i):
                    k.append(int(m))
                if sorted(c)==k:
                    total += 1
            

    return total

print(count(2))