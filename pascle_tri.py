
"""
This is for convert array to digits.
"""
# This is the first methode 
def fav(n):
    s = 0
    j = 0
    # l = len(n)
    for i in n:
        if j!=(len(n)-1):
            s += i
            s *= 10
        else:
            s += i
        j += 1
    return s

print(fav([1, 6, 1, 0, 5, 1]))


# This is the second method

def converting(n):
    s = ''
    for i in n:
        s += str(i)

    return int(s)

print(converting([1, 6, 1, 0, 5, 1]))


# This is the solution for pascal triangle in leetcode

class Solution:
    def generate(self, numRows):
        r = []
        for i in range(numRows):
            r.append([])
            r[i].insert(0, 1)
            r[i].insert(i, 1)
            for j in range(1, i+1):
                r[i].insert(j, r[i-1][j-1]+r[i-1][j])

        r.insert(0, [1])
        return r[0:numRows]

s = Solution()
print(s.generate(3))