from typing import List
import math
class Solution:
    def climbStairs(self, n: int) -> int:
        st, nd = 1, 1
        for idx in range(n):
            st, nd = (st+nd), st
        return nd
slt = Solution()
"""
n = 1 
    a : a + b = (1 + 1) = 2
    b : pre_a = 1 = ans
n = 2 
    a : a + b = (2 + 1) = 3
    b : pre_a = 2 = ans
n = 3 
    a : a + b = (3 + 2) = 5
    b : pre_a = 3 = ans
n = 4 
    a : a + b = (5 + 3) = 8
    b : pre_a = 5 = ans
n = 5 
    a : a + b = (8 + 5) = 13
    b : pre_a = 8 = ans
n = 6 
    a : a + b = (13 + 8) = 21
    b : pre_a = 13 = ans
    
"""
slt.climbStairs(45)
"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
 
Constraints:
    1 <= n <= 45
"""