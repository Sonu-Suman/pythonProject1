# This is the first problem.
"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) 
extra memory.




*Custom Judge:
--------------------
The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


"""
class Solution:
    def removeDuplicates(self, nums) -> int:

        N = len(nums)
        if N==0 or N ==1:
            return N
        
        start, cnt, prev = -1, 0, None
       
        for end in range(N):
            val = nums[end]
            if nums[end]!=prev:
                start+=1
                nums[start], nums[end] = nums[end], nums[start]
                cnt+=1
                
            prev = val
            
        return cnt, nums


arr = [1, 2, 2, 2, 3, 4, 5, 5, 6]
s = Solution()
print(s.removeDuplicates(arr))


# This is the second method but this is only working on even repeatable elements

def remove(arr):
    l = len(arr)
    prev = None
    for i in range(l):
        current = arr[i]
        if current == prev:
            arr.remove(arr[i])
            arr.append(current)
        prev = current

    return arr


arr = [1, 2, 2, 3, 4, 5, 5, 6]
print(remove(arr))


# THis is the second problem

"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) 
extra memory.



Custom Judge:
-----------
The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.
"""


class Solution:
    def removeElement(self, nums, val):
        n = len(nums)
        if n==0:
            return 0

        
        for i in nums[::-1]:
            nums.remove(i)
            if i !=val:
                nums.append(i)


        return nums, len(nums)

arr = [1, 2, 2, 3, 4, 5, 5, 6]
val = 2
s = Solution()
print(s.removeElement(arr, 5))