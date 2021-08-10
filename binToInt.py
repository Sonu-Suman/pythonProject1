"""
Given two binary strings a and b, return their sum as a binary string.


Example 1:

Input: a = "11", b = "1"
Output: "100"

"""

# This is first approach

def binaryTOinteger(binary):
    l = []
    j = 0
    if int(binary[-1])==1:
        j += 1

    if int(binary[:-1])!=0:
        s = 0
        ar = binary[:-1]
        for i in ar[::-1]:
            if int(i)==1:
                s+=1
                j += 2**(s)
            elif int(i)==0:
                s += 1
        l.append(j)

print(binaryTOinteger("11"))


# This is Second Approach

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = int(a, 2)
        s1 = int(b, 2)
        
        return format(s+s1, 'b')