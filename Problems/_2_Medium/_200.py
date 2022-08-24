from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1's (land) and '0's (water),
        visited = set()
        # → ↓ ← ↑
        dirs = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        def bfs(c, m, n):
            dq = deque([c])
            while dq:
                cord = dq.popleft()
                if cord in visited: continue
                visited.add(cord)
                for d_r, d_c in dirs:
                    r = cord[0] + d_r
                    c = cord[1] + d_c
                    if 0 <= r < m and 0 <= c < n and grid[r][c] != "0":
                        dq.append((r, c))  
        count = 0
        # O(m * n)
        m, n = len(grid) , len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0" or (i,j) in visited: continue
                bfs((i,j), m, n)
                count += 1
        print(count)
        return count
slt = Solution()
cases = [
    [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]],
    [["1"]],
    [["0"]],
    [ ["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"],["0","0","0","1","1"]],
]
# Test Case
for grid in cases:
    slt.numIslands(grid)

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and 
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 You may assume all four edges of the grid are all surrounded by water.

 

Example 1:
    Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:
    Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

"""