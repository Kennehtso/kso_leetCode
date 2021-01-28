from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, d in enumerate(nums, start=0):
            d_st, idx_st = d, idx
            d_nd = target-d_st
            if d_nd == d_st:
                nums_chk = nums.copy()
                nums_chk.remove(d_st)
                if d_nd in nums_chk :
                    r = [idx_st, nums_chk.index(d_nd)+1 ]
                    print(r)
                    return r
            elif d_nd != d_st and d_nd in nums:
                r = [idx_st, nums.index(d_nd)]
                print(r) 
                return r
            continue    
        return []
        """ # Most voted 
        h = {}
        for i, num in enumerate(nums):
            n = target - num 
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]  """
slt = Solution()
"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Constraints:
    2 <= nums.length <= 103
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
"""
# Test Case
result=slt.twoSum([3,2,3],6)
result=slt.twoSum([3,2,4],6)
result = slt.twoSum([1,222,34,22,13,123,55,1,2,7,126,2,3,3,78,45,6,6,2,5,2,6,856,7,2,65,23,23,23,56,4],869)