from typing import List
import math
class Solution:
    def climbStairs(self, n: int) -> int:
        """ if n == 1: return 1
        elif n == 2: return 2
        r, a, b = 0, 1, 2
        for i in range(3, n+1):
            r = a + b
            a = b
            b = r
        """
        sqrt5 = math.sqrt(5)
        fibn = pow((1+sqrt5)/2, n+1) - pow((1-sqrt5)/2, n+1)
        r = (int)(fibn/sqrt5)
        print(r) 
        return r
slt = Solution()
slt.climbStairs(127642)
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
 
5
1,1,1,1,1
5-2=3-2=1
1,1 -> 1
2,2 -> 1,1, 2
3,3 ->-3 1,1,1, 1,2, 2,1 
4,5 ->-3 1,1,1,1 1,1,2, 1,2,1, 2,1,1, 2,2 
5,8  +1
6,13 -2
7,21 
-> 0,
 4 -> 1, +2 * 2+0
5 ->3, +4 2 *3 +1
6 -> 7,+7 2 * 
7 -> 14, +12
8 -> 26
    1,1,1,1,1 ,0 of 2, 5^0 = 1
    1,1,1,2,  = 4
    1,2,2 = 3

6
1,1,1,1,1,1  = 1
1,1,1,1,2 = 5
1,1,2,2 = 6
2,2,2 = 1



1122
1221
2211
2121
1212
2112

Constraints:
    1 <= n <= 45
"""