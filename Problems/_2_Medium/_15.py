from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for st in range(len(nums)):
            if st > 0 and nums[st] == nums[st-1]: continue
            #1. Try always 0 to len(nums) X Fail, will have duplicate, not worth to handle it with more time
            #2. Try idx+1 to end, much better solution especially is sorted already, no need to care for the left side
            nd, rd = st+1, len(nums)-1
            while nd < rd:
                #print("nd, rd: ",nd, rd)
                addUp = nums[st] + nums[nd] + nums[rd]
                if addUp > 0 : rd -= 1
                elif addUp < 0 : nd += 1
                else:
                    #print("st, nd rd = %s, %s, %s:"%(st, nd, rd))
                    res.append([nums[st], nums[nd], nums[rd]])
                    nd += 1
                    while  nums[nd] == nums[nd-1] and nd < rd:
                        nd += 1
        #print("res: ",res)
        return res
        
        # Thoughts:
        # st + nd + rd = 0
        # -5 -5 -3 -1 0 2 3 4 4 4 5
        # -5 -3 -1 0 2 3 4 5

         
slt = Solution()    
# Test Case
slt.threeSum(nums = [-1,0,1,2,-1,-4])

"""
15. 3Sum
Medium
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

 
Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

Example 2:
    Input: nums = []
    Output: []

Example 3:
    Input: nums = [0]
    Output: []


Constraints:
    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105

Runtime: 844 ms, faster than 80.86% of Python3 online submissions for 3Sum.
Memory Usage: 18 MB, less than 66.03% of Python3 online submissions for 3Sum.
"""
