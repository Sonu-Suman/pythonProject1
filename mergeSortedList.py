"""
88. Merge Sorted Array


You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

nums1 = [1, 0, 2, 0, 3, 0, 0, 0]
nums2 = [2,5,6]
m =3
n = 3

def f( nums1, m, nums2, n):
    if nums1[:m].count(0)!=0:
            l = len(nums1)
            for i in nums1:
                if i !=0:
                    nums1.append(i)
                    if len(nums1)== l+m:
                        j = 0
                        if nums2 != []:
                            for i in nums2:
                                if i!=0:
                                    nums1.append(i)
                                    j += 1
                                    if j==n:
                                        return sorted(nums1[l:l+m+n])
                        else:
                            return nums1[l:l+m]
    else:
        l = len(nums1)
        for i in nums1:
            nums1.append(i)
            if len(nums1)== l+m:
                j = 0
                if nums2 != []:
                    for k in nums2:
                        if k!=0:
                            nums1.append(k)
                            j += 1
                            if j==n:
                                return  sorted(nums1[l:l+m+n])
                else:
                    return nums1[l:l+m]
  


print(f(nums1, m, nums2, n))


# This is the second approach

def find(nums1, m , nums2, n):
    # last index of nums1
    last = n+m -1

    # merge in reverse order
    while n>0 and m>0:
        if nums1[m-1]>nums2[n-1]:
            nums1[last] = nums1[m-1]
            m -= 1
        else:
            nums1[last] = nums2[n-1]
            n -= 1
        last -= 1

    while n>0:
        nums1[last] = nums2[n-1]
        n, last = n-1, last-1

        