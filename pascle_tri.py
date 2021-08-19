"""
I build this when i tried to solve pascle triangle problem.
this is only aplicable for 4 for lines.
"""

class Solution:
    l = []
    def generate(self, numRows):
        assert numRows==int(numRows), 'Please must be enter digit.'
        
        def fav(n):
            j = 0
            for i in n:
                if i == 0:
                    if j!=(len(n)-1):
                        n[j-1] = n[j-1]*10
                        n.remove(i)

                j += 1

            return n
        
        if numRows==0:
            s = self.l.copy()
            self.l.clear()
            return s[::-1]
        
        self.l.append(fav([int(i)for i in str(11**(numRows-1))]))
        return self.generate(numRows-1)


s = Solution()
print(s.generate(7))



"""
This is for convert array to digits.
"""

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