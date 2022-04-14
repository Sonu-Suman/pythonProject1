# Number of n-digits non-decreasing integers

"""
Given an integer n > 0, which denotes the number of digits, 
the task to find the total number of n-digit positive integers which are non-decreasing in nature. 
A non-decreasing integer is one in which all the digits from left to right are in non-decreasing form. ex: 1234, 1135, ..etc. 
Note: Leading zeros also count in non-decreasing integers such as 0000, 0001, 0023, etc are 
also non-decreasing integers of 4-digits. 
ex : -
input:
----------------
 n = 2

Output:
-----------------
55

explanation :
--------------------
0 - 10 = 10
11 - 20 = 9
21 - 30 = 8
31 - 40 = 7
41 - 50 = 6
51 - 60 = 5
61 - 70 = 4
71 - 80 = 3
81 - 90 = 2
91 - 99 = 1
-------------------
Total = 55

"""

# This is the solution

def count(n):
    total = 10
    if n<1:
        return 0

    for i in range(10, int('9'*n)+1):
        if sorted(list(str(i))) == list(str(i)):
            total += 1
            
    return total


print(count(1))