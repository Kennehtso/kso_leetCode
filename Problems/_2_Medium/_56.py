from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        print("Before : %s"%(intervals))
        intervals.sort()
        ptr, start, end = 1, 1, len(intervals)
        pre = intervals[0]
        while start < end:
            cur = intervals[ptr]
            # No overlap
            if cur[0] > pre[1]:
                pre = cur
                ptr += 1
            else:
                # has overlap
                # Combine, move forward
                s = min(cur[0], pre[0])
                e = max(cur[1], pre[1])
                pre = intervals[ptr - 1] = [s, e]
                intervals.pop(ptr)
            start += 1
        print("after : %s"%(intervals))
        return intervals
         
slt = Solution()
cases = [
    [[1,3],[17,18],[1,3],[2,6],[8,10],[15,18]],
    [[1,3],[2,4]],
    [[1,3],[2,3]],
    [[1,3],[3,4]],
    [[1,2],[3,4]],
    [[1,4],[2,3]],
    [[1,4]]
]
# Test Case
for intervals in cases:
    slt.merge(intervals)

"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
================================================================================================================
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
-2, -2 +1, 1
-1, 1, -3, 
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [0]
Output: 0

Example 4:
Input: nums = [-1]
Output: -1

Example 5:
Input: nums = [-100000]
Output: -100000
================================================================================================================

Constraints:
    1 <= nums.length <= 3 * 10^4
    -10^5 <= nums[i] <= 10^5
"""
""" 
#=====Draft=====
  if len(nums) is 1:
            return nums[0]
        pre = nums[0]
        contiguousTotal = nums[0]
        contiguousList = []
        for idx in range(1, len(nums)):
            cur = nums[idx]
            roundTotal_By_2_nums = pre + cur #4 + -1 == 3
            roundTotal_By_2_Total = contiguousTotal + cur #1 + -1 == 0

            if roundTotal_By_2_nums < contiguousTotal and roundTotal_By_2_Total < contiguousTotal:
                options[contiguousTotal] = contiguousList
                contiguousList = []
                if roundTotal_By_2_Total > roundTotal_By_2_nums:
                    # due to sum is smaller than in the dict
                    roundTotal_By_2_Total = 0 #init
              
            if roundTotal_By_2_Total < roundTotal_By_2_nums:
                if len(contiguousList) >=2:
                    contiguousList.pop(0)
                else:
                    contiguousList.append(pre)

                contiguousList.append(cur)
                contiguousTotal = roundTotal_By_2_nums
                #and???
            elif roundTotal_By_2_Total >= roundTotal_By_2_nums:
                if idx == 1:
                    contiguousList.append(pre)
                contiguousList.append(cur)
                contiguousTotal = roundTotal_By_2_Total
                if contiguousTotal not in options:
                    options[contiguousTotal] = contiguousList
            pre = cur
            
        print(options)
        maxNum = max(nums)
        if len(options) > 0 :
            maxKey = max(options)
            if len(options[maxKey]) is not 0 and maxKey > maxNum:
                maxNum = maxKey
                print(f"Max SubArray is : {options[maxNum]}")
        print(f"Max Num {maxNum}")
        return maxNum
"""