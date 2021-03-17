from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val) > 0:
            nums.pop(nums.index(val))

slt = Solution()    
# Test Case
slt.removeElement([0,1,2,2,3,0,4,2])
"""
27. Remove Element
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Constraints:
    0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100


"""
