"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the 
given set with sum equal to given sum. 

Example: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
"""

#---------------------------------------------------------------
# This is the first method.

def finding_subset(su, sum):
	s = {}

	if sum==0:
		return True
		

	for i in range(len(su)):
		if su[i]<=sum:
			s[su[i]] = [0]
			for j in range(i+1, len(su)):
				d = su[i] + su[j]
				s[su[i]].append(d)
				if d==sum:
					return "Yes, we found that pair", (su[i], su[j])
	return "pair don't exist."


print(finding_subset([3, 34, 15, 4, 12, 5, 2], 9))


#------------------------------------------------------------------------------
# This is the second method.

def finding_pair_sum(su, sum):

    if sum==0:
        return True
        
    for i in range(len(su)):
        if su[i]==sum:
            return 0, su[i]
        elif su[i]<sum:
            for j in range(i+1, len(su)):
                if su[i]+su[j]==sum:
                    return su[i], su[j]

    return "Pair don't exist in the list"

    
print(finding_pair_sum([3, 34, 15, 4, 12, 5, 2], 30))


#----------------------------------------------------------------
# This is third method.

# A recursive solution for subset sum problem

# Returns true if there is a subset of set[] with sun equal to given sum

def isSubsetSum(set, n, sum):

	# Base Cases
	if (sum == 0):
		return True
	if (n == 0):
		return False

	# If last element is greater than
	# sum, then ignore it
	if (set[n - 1] > sum):
		return isSubsetSum(set, n - 1, sum)

	# else, check if sum can be obtained
	# by any of the following
	# (a) including the last element
	# (b) excluding the last element
	return isSubsetSum(
		set, n-1, sum) or isSubsetSum(
		set, n-1, sum-set[n-1])


# Driver code
set = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set)
if (isSubsetSum(set, n, sum) == True):
	print("Found a subset with given sum")
else:
	print("No subset with given sum")


# ----------------------------------------------------------------------------------
# This is for fourth problem methode.

# A Dynamic Programming solution for subset sum problem Returns true if there is a subset of
# set[] with sun equal to given sum

# Returns true if there is a subset of set[] with sum equal to given sum
def isSubsetSum(set, n, sum):
	
	# The value of subset[i][j] will be
	# true if there is a
	# subset of set[0..j-1] with sum equal to i
	subset =([[False for i in range(sum + 1)]
			for i in range(n + 1)])
	
	# If sum is 0, then answer is true
	for i in range(n + 1):
		subset[i][0] = True
		
	# If sum is not 0 and set is empty,
	# then answer is false
	for i in range(1, sum + 1):
		subset[0][i]= False
			
	# Fill the subset table in bottom up manner
	for i in range(1, n + 1):
		for j in range(1, sum + 1):
			if j<set[i-1]:
				subset[i][j] = subset[i-1][j]
			if j>= set[i-1]:
				subset[i][j] = (subset[i-1][j] or
								subset[i - 1][j-set[i-1]])
	
	# uncomment this code to print table
	# for i in range(n + 1):
	# for j in range(sum + 1):
	# print (subset[i][j], end =" ")
	# print()
	return subset[n][sum]
		
# Driver code
if __name__=='__main__':
	set = [3, 34, 4, 12, 5, 2]
	sum = 9
	n = len(set)
	if (isSubsetSum(set, n, sum) == True):
		print("Found a subset with given sum")
	else:
		print("No subset with given sum")


# ____-----------------------------------------------------------------------
# This is fifth solution method.

# Python program for the above approach

# Taking the matrix as globally
tab = [[-1 for i in range(2000)] for j in range(2000)]

# Check if possible subset with
# given sum is possible or not
def subsetSum(a, n, sum):
	
	# If the sum is zero it means
	# we got our expected sum
	if (sum == 0):
		return 1
	
	if (n <= 0):
		return 0
		
	# If the value is not -1 it means it already call the function with the same value.
	# it will save our from the repetition.
	if (tab[n - 1][sum] != -1):
		return tab[n - 1][sum]
		
	# if the value of a[n-1] is greater than the sum.
	# we call for the next value
	if (a[n - 1] > sum):
		tab[n - 1][sum] = subsetSum(a, n - 1, sum)
		return tab[n - 1][sum]
	else:
		
		# Here we do two calls because we don't know which value is full-fill our criteria
		# that's why we doing two calls
		tab[n - 1][sum] = subsetSum(a, n - 1, sum)
		return tab[n - 1][sum] or subsetSum(a, n - 1, sum - a[n - 1])

# Driver Code

n = 5
a = [1, 5, 3, 7, 4]
sum = 12

if (subsetSum(a, n, sum)):
	print("YES")
else:
	print("NO")


# This is the sixth method

def findPair(arr, target):
	if len(arr)==0:
		return 0

	if target==0:
		return 1
	for i in range(len(arr)-1):
		s = target-arr[i]
		if s in arr[i+1:]:
			return "Yes, we found the pair."
	return "Pair doesn't exist in the list."


a = [1, 5, 3, 7, 4]
sum = 12

print(findPair(a, sum))