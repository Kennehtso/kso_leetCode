from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        [
            [0 ,0 ,0 ,0 ,0],
            [0, 1, 1, 0, 0],
            [1, 1, 1 ,1 ,1],
            [0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1]]
        """
        # Set all '0' to visited,
        # expand it to dq, 
        checked = set()
        from collections import deque
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    checked.add((i,j))
                    q.append((i,j))
        #check for its 4 dirs 
        # 1. if it's dir 1/2/3/4 not in visited, plus 1 by itself,
        # 1.1 start with 0, so it 4 dirs should be 0 + 1, 
        # 1.2 then add them to q, they will be value with 1
        # once loop to the first non 0 cell, itself + 1 = 2, then repeat to spread out to the end.
        while q:
            x,y = q.popleft()
            # right, left, up, down
            for dirr in [(1,0), (-1,0), (0,1), (0,-1)]:
                newX, newY = x+dirr[0], y+dirr[1]
                if newX >= 0 and newX <= len(mat)-1 and newY >= 0 and newY <= len(mat[0])-1 and (newX, newY) not in checked:
                        print("parent (x, y) : (%s, %s)"%(x,y))
                        print("newX, newY : (%s, %s)"%(newX, newY))
                        mat[newX][newY] = mat[x][y] + 1
                        print("mat[newX][newY] : %s"%(mat[newX][newY]))
                        checked.add((newX, newY))
                        q.append((newX, newY))
        print(mat)
        return mat

slt = Solution() 
# Test Case
slt.updateMatrix([[0 ,0 ,0 ,0 ,0],[0, 1, 1, 0, 0], [1, 1, 1 ,1 ,1],[0, 1, 1, 1, 1], [0, 1, 1, 1, 1]])
"""
542. 01 Matrix
Medium
Given an m x n binary matrix mat, 
return the distance of 
the nearest 0 for each cell.
The distance between two adjacent cells is 1.



Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

 

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 104
    1 <= m * n <= 104
    mat[i][j] is either 0 or 1.
    There is at least one 0 in mat.

"""