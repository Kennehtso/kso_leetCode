from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count, rge = 0, len(nums)-1
        nums.sort()
        for idx in range(rge, 0, -1):
            count += nums[idx]-nums[0]
        print(count)
        return count
        
slt = Solution()    
# Test Case
slt.minMoves([4,7,2,1,2,1,3])
#slt.minMoves([1,2147483647])
[1, 1, 2, 3, 4, 7, 8]

"""
453. Minimum Moves to Equal Array Elements

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
Example:
    Input:
      [1,2,3]
    Output:
      3
    Explanation:
        Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""
