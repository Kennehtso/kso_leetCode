from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        t, r = 0, []
        for n in nums:
            t += n
            r.append(t)
        print(r)
        return r

        # Following with Single-line but slow, due to sum need to caculate every time enter the loop. 
        # return [sum(nums[0:idx+1]) for idx in range(0, len(nums))]
            
        
slt = Solution()
slt.runningSum([1,1,1,1,1,1])

"""
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.


Example 1:
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
    Input: nums = [1,1,1,1,1]
    Output: [1,2,3,4,5]
    Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
    Input: nums = [3,1,2,10,1]
    Output: [3,4,6,16,17]

Constraints:
    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6

"""
