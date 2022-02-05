"""
Given three numbers n, r and p, compute value of nCr mod p. 
Example: 

Input:  n = 10, r = 2, p = 13
Output: 6
Explanation: 10C2 is 45 and 45 % 13 is 6.
"""

#-------------------------------------------------------------------
# This is first type of code

def nCr_P(n, r, p):
	tab = [0]*(n+1)

	tab[0] =1
	for i in range(1, n+1):
		tab[i] = (tab[i-1]*i)

	cal = int(tab[n]/(tab[r]*tab[(n-r)]))

	return cal%p


print(nCr_P(5, 3, 1000000007))


#--------------------------------------------------------------------------
# This is second type of code

# A Dynamic Programming based solution to compute nCr % p

# Returns nCr % p
def nCrModp(n, r, p):

	# Optimization for the cases when r is large
	# compared to n-r
	if (r > n- r):
		r = n - r

	# The array C is going to store last row of
	# pascal triangle at the end. And last entry
	# of last row is nCr.
	C = [0 for i in range(r + 1)]

	C[0] = 1 # Top row of Pascal Triangle

	# One by constructs remaining rows of Pascal
	# Triangle from top to bottom
	for i in range(1, n + 1):

		# Fill entries of current row
		# using previous row values
		for j in range(min(i, r), 0, -1):

			# nCj = (n - 1)Cj + (n - 1)C(j - 1)
			C[j] = (C[j] + C[j-1]) % p

	return C[r]

# Driver Program
n = 10
r = 2
p = 13
print('Value of nCr % p is', nCrModp(n, r, p))
