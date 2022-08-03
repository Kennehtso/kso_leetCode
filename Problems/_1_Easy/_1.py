from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        chk = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in chk:
                return [chk[diff], idx]
            chk[num] = idx

slt = Solution()
"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Constraints:
    2 <= nums.length <= 10^3
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.
"""
# Test Case
result=slt.twoSum([3,2,3],6)
result=slt.twoSum([3,2,4],6)
result = slt.twoSum([1,222,34,22,13,123,55,1,2,7,126,2,3,3,78,45,6,6,2,5,2,6,856,7,2,65,23,23,23,56,4],869)