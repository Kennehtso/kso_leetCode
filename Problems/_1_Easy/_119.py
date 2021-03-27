from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        elif rowIndex == 1: return [1,1]
        pre, work = [1,1], []
        for idx in range(2 ,rowIndex+1):
            work.clear()
            work.append(1)
            tmp = pre[0]
            for idx2 in range(1, len(pre)):
                work.append(tmp+pre[idx2])
                tmp = pre[idx2]
            work.append(1)
            pre = work.copy()
        return pre

slt = Solution()
# Test Case
slt.getRow([1,3,3,1])
"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
    Input: rowIndex = 3
    Output: [1,3,3,1]

Example 2:
    Input: rowIndex = 0
    Output: [1]

Example 3:
    Input: rowIndex = 1
    Output: [1,1]

Constraints:
    0 <= rowIndex <= 33


Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

"""