"""
Share
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

# This is the first approach and this approach take more time.

from itertools import permutations, combinations


def find(nums):
    if len(nums)==sum(nums):
        return 1
    else:
        return len(set(permutations(nums)))
        


 # print(find([2, 2, 1, 1, 1]))


digits = 1
l = []
n = 7
for i in range(1, (n//2)+1):
    [l.append(2) for j in range(i)]
    [l.append(1) for k in range(n-2*(i))]
    digits += find(l)
    l.clear()

print(digits)

# This is second approach with less lines of code

def climbStairs(self, n: int) -> int:
        digits = 1
        l = []

        for i in range(1, (n//2)+1):
            [l.append(2) for j in range(i)]
            [l.append(1) for k in range(n-2*(i))]
            digits += len(set(permutations(l)))
            l.clear()
        
        return digits


# This is the forth approach and this methode is much more time efficient

def findStair(n):
    if n==1 or n==2 or n==3:
        return n
    else:
        dic = {3:3, 4:5}
        for i in range(5, n+1):
            dic[i] = dic.get(i-1)+dic.get(i-2)
                
    return dic.get(n)
        


print(findStair(20000))
