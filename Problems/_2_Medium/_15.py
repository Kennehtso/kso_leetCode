from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        r = []
        S = sorted(nums)
        #print(S)
        for idx in range(0, len(nums)-2):
            if idx == 0 or (idx > 0 and S[idx] != S[idx-1]): 
                lo = idx + 1
                hi = len(S)-1
                while lo < hi:
                    _sum = S[idx] + S[lo] + S[hi]
                    if _sum == 0:
                        r.append([S[idx], S[lo] ,S[hi]])
                        #print("a, low, high: " ,S[idx], S[lo] ,S[hi])
                        while lo < hi and S[lo+1] == S[lo] : lo+=1 ### KEY lo < hi go first prevent out of range
                        while lo < hi and S[hi-1] == S[hi] : hi-=1 ### KEY  
                        #lo += 1
                        hi -= 1
                        #print("lo+=1 : ", lo)
                        #print("hi+=1 : ", hi)
                    elif _sum > 0:  hi -= 1 ### KEY S[idx] + S[lo] + S[hi] > 0
                    else : lo += 1  ### KEY S[idx] + S[lo] + S[hi] < 0
                        
        print(r)
        return r

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
