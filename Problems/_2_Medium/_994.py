from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        dirs = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        level, fresh = 0, 0
        dq = deque([])
        #initiailize
        # O(m x n))
        for i in range(m):
            for j in range(n):
                # if is rotten from start, push to dq
                if grid[i][j] == 2 : dq.append(((i,j),0))
                # if is fresh from start, fresh += 1
                elif grid[i][j] == 1 : fresh += 1
        # O(n))
        while dq:
            cord, lv = dq.popleft()
            level = max(level, lv)
            if cord in visited: continue
            visited.add(cord)
            for d_r, d_c in dirs:
                r = d_r + cord[0]
                c = d_c + cord[1]
                # only add in bound, and fresh orange to dq
                if not(0 <= r < m and 0 <= c < n and (r,c) not in visited and grid[r][c] == 1):
                    continue
                # set fresh to rotten now, add to dq to spread.
                # decrease the fresh amount
                grid[r][c] = 2
                dq.append(((r, c), lv + 1))
                fresh -= 1
        return level if fresh == 0  else -1

slt = Solution() 
# Test Case
cases = [
    [[2,1,1],[1,1,0],[0,1,1]],
    [[2,1,1],[0,1,1],[1,0,1]],
    [[0, 2]]
]
# Test Case
for grid in cases:
    slt.numIslands(grid)

slt.orangesRotting()
"""
994. Rotting Oranges
Medium

You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.

"""