from collections import deque
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # - * - = + >>> <<< + * + = + 
        start, end = 0, len(nums) - 1
        dq = deque([])
        while start <= end:
            left = nums[start] * nums[start]
            right = nums[end] * nums[end]
            if left >= right:
                dq.appendleft(left)
                start += 1
            else:
                dq.appendleft(right)
                end -=1
        return dq

slt = Solution()    
# Test Case
slt.sortedSquares([-7,-3,2,3,11])

"""
977. Squares of a Sorted Array

Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].

Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]
 
Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.
"""
