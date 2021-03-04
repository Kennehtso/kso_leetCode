from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        elif numRows == 2: return [[1],[1,1]]
        r, r_pre = [[1]], [1,1]
        r.append(r_pre)
        for idx in range(3, numRows+1):
            curArr = [1]
            pre_v = r_pre[0]
            for idx2 in range(1, len(r_pre)):
                cur = r_pre[idx2]
                curArr.append(pre_v + cur)
                pre_v = cur
            curArr.append(1)
            r.append(curArr)
            r_pre = curArr
        print(r)
        return r
            
slt = Solution()
# Test Case
slt.generate(5)
"""
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
    Input: numRows = 1
    Output: [[1]]
    

Constraints:
    1 <= numRows <= 30
"""