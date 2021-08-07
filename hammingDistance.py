# THIS IS GOOGLE PROBLEM

"""Problem Description

Hamming distance between two non-negative integers is defined as the number 
of positions at which the corresponding bits are different.

Given an array A of N non-negative integers, find the sum of hamming distances 
of all pairs of integers in the array. Return the answer modulo 1000000007."""

# This is the basic question of this topic
def hammingDistance(n1, n2) :
 
    x = n1 ^ n2
    setBits = 0
 
    while (x > 0) :
        setBits += x & 1
        x >>= 1
     
    return setBits
 
if __name__=='__main__':
    n1 = 9
    n2 = 14
    print(hammingDistance(9, 14)) 
    

# This is first Approach to solve the problem and this take long time

class Solution:
    def hammingDistance(self, A):
        d = 0
        if len(A)<=1:
            return 0

        for i in range(len(A)):
            for j in range(len(A)):
                if i<len(A)-1:
                    if i+j<len(A):
                        if A[i+j]!=A[i]:
                            s = list(str(format(A[i]^A[i+j], 'b')))
                            s2 = list(str(format(A[i+j]^A[i], 'b')))
                            d += s.count('1')
                            d += s2.count('1')
        if d == 0:
            return 0
        else:
            return d%1000000007


s = Solution()
print(s.hammingDistance([2, 3, 4]))


# This is second Approach and this algorithm is time efficient

def hammingDistance(A):
    l = []
    for i in A:
        l.append('{:032b}'.format(i))
        # print('{:032b}'.format(i))
    c=0
    print(l)
    l=list(zip(*l))
    print(l)
    for i in l:
        a=i.count('0')
        b=i.count('1')
        # print(2*a*b)
        c+=(2*a*b)
    return (c%1000000007)


print(hammingDistance([2, 3, 4]))