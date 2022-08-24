from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use prefix + post fix array
        l = len(nums)
        ans = [1] * l
        prefix = postfix = 1
        # set ans by prefix
        for i in range(l):
            ans[i] = prefix
            prefix *= nums[i]
        # update ans[i] with prefix * postfix
        for i in range(l-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans
        """
        # *** The following is not allow to use dividing operator0
        l = len(nums)
        answer = [0] * l
        # edge case 1, if > 1 zero, all 0 
        if 0 in nums and nums.count(0) > 1: 
            print(answer)
            return answer
        total = 1
        for n in nums:
            if n == 0: continue
            total *= n
        # edge case 2, if == 1 zero, except index of 0 will be total, others 0 
        if 0 in nums and nums.count(0) == 1:
            answer[nums.index(0)] = total
            print(answer)
            return answer
        # normal case, no zero
        for idx in range(l): 
            answer[idx] = total//nums[idx]
        print(answer)
        return answer
        """
slt = Solution() 
# Test Case
slt.productExceptSelf([1,2,3,4])
"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:
    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
"""