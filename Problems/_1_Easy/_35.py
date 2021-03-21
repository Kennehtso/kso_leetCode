from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for idx, num in enumerate(nums):
            #print(f"{idx} of {num}")
            if target > num:
                continue
            else:
                return idx
        return len(nums)

slt = Solution()    
# Test Case
slt.searchInsert(nums = [1,3,5,6], target = 0)
"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, 
return the index where it would be if it were inserted in order.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 5:
    Input: nums = [1], target = 0
    Output: 0

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.

"""
