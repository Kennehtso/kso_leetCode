from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums: return 1
        r = float('inf')
        sum_ = 0
        slowPtr = 0
        for idxPtr in range(len(nums)):
            sum_ += nums[idxPtr]
            while sum_ >= target:
                # [0, 1, 2, 3, 4]
                r = min(r, idxPtr - slowPtr + 1)
                sum_ -= nums[slowPtr]
                slowPtr += 1
            if r == 2: break
        return 0 if r == float('inf') else r

slt = Solution()    
# Test Case
slt.minSubArrayLen(7, [1,3,2,4,5,1,6])

"""
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of 
which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
    Input: target = 4, nums = [1,4,4]
    Output: 1

Example 3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0

Constraints:
    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 105

"""