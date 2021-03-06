from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        nums.sort()
        for num in nums:
            if num not in d: d[num] = 1
            else: d[num] +=1
        return [k for k,v in d.items() if v > len(nums)/3]

slt = Solution()    
# Test Case
slt.majorityElement([3,2,3])
"""
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Follow-up: Could you solve the problem in linear time and in O(1) space?

Example 1:
    Input: nums = [3,2,3]
    Output: [3]

Example 2:
    Input: nums = [1]
    Output: [1]

Example 3:
    Input: nums = [1,2]
    Output: [1,2]

Constraints:

    1 <= nums.length <= 5 * 104
    -109 <= nums[i] <= 109

"""
