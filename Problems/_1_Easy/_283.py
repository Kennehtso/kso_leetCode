from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda e: e==0)
        """
        c = nums.count(0)
        while c > 0:
            i = nums.index(0)
            nums.pop(i)
            nums.append(0)
            c-=1
        #print(f"nums: {nums}")
        """
        
slt = Solution()
# Test Case
#result = slt.longestCommonPrefix(["dog","racecar","car"])
slt.moveZeroes([0,1,0,3,12])


"""
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""