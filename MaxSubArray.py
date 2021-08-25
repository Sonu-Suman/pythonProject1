"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""

# This is the first approach and this approach take O(n^2) time

class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        
        m = 0
        ans = []
        k = []
        for i in range(len(nums)):
            k.append(nums[i])
            m = nums[i]
            ans.append(m)
            for j in range(i+1, len(nums)):
                k.append(nums[j])
                m += nums[j]
                ans.append(m)

        return max(ans)


s = Solution()

print(s.maxSubArray([5,4,-1,7,8]))


# THis is the second approach

def maxSubArray(nums):
    s = 0
    l = []
    for i in range(len(nums)):
        l.append(nums[i])
        for j in range(i+1, len(nums)):
            l.append(nums[j])
            if sum(l)>s:
                s=sum(l)
        l.clear()

    return s



print(maxSubArray([5,4,-1,7,8]))

# This is third approach and this take O(n)

def maxSubArray(nums):
    s = 0
    l = 0
    for i in range(len(nums)):
        l+=nums[i]

        if l>s:
            s=l

        if l<0:
            l=0

    return s


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# This is the forth Approach 

class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)
        
        minPreSum = preSum[0]
        ans = nums[0]
        for i in range(1, n + 1):
            ans = max(ans, preSum[i] - minPreSum)
            minPreSum = min(minPreSum, preSum[i])

        return ans
        

s = Solution()
print(s.maxSubArray([-2,-1]))


# This is the fifth type

import sys

def smallestSumSubarr(arr, n):
    max_ending_here = -sys.maxsize - 1
     
    max_so_far = -sys.maxsize - 1
     
    for i in range(n):
        if (max_ending_here > 0):
            max_ending_here += arr[i]
         
        # else add the value arr[i] to max_ending_here
        else:
            max_ending_here = arr[i]
          
        # update max_so_far
        max_so_far = max(max_so_far, max_ending_here)
     
    # required biggest sum contiguous subarray value
    return max_so_far


print(smallestSumSubarr([-2, -3, 4, -1, -2, 1, 5, -3], 8))