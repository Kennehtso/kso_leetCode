from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right
        
class Solution:
    def findLast(self, nums: List[int], target: int):
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = (left + right ) //2
            if nums[mid] <= target:
                last = mid
                left = mid + 1
            else:
                right = mid - 1
        return last
    
    def findFirst(self, nums: List[int], target: int):
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right ) //2
            if nums[mid] >= target:
                first = mid
                right = mid - 1
            else:
                left = mid + 1
        return first
        
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1,-1]
        elif target not in nums: return [-1,-1]
        print( [self.findFirst(nums, target), self.findLast(nums, target)])
        return [self.findFirst(nums, target), self.findLast(nums, target)]
        


slt = Solution()    
# Test Case
slt.searchRange(nums = [5,7,7,8,8,10], target = 8)

"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

 

Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]



Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109

"""