from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l, nums= len(nums), set(nums)
        print(nums)
        for idx in range(1, l+1):
            if idx in nums:
                nums.remove(idx)
            else:
                nums.add(idx)
        print(nums)
        return list(nums)

slt = Solution()    
# Test Case
slt.findDisappearedNumbers([4,3,2,7,8,2,3,1])

"""
448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
    Input:
    [4,3,2,7,8,2,3,1]
    Output:
    [5,6]
"""
