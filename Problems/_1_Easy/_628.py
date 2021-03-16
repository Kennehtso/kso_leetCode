from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        right = nums[-3] * nums[-2] * nums[-1]
        left = nums[0] * nums[1] * nums[-1] # These use the last one because use nums[2] if < 0 will become lowest.
        return max(left, right)
        
slt = Solution()    
# Test Case
slt.maximumProduct([-1,-2,-3])

"""
628. Maximum Product of Three Numbers

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.


Example 1:
  Input: nums = [1,2,3]
  Output: 6

Example 2:
  Input: nums = [1,2,3,4]
  Output: 24

Example 3:
  Input: nums = [-1,-2,-3]
  Output: -6

Constraints:
    3 <= nums.length <= 104
    -1000 <= nums[i] <= 1000


"""
