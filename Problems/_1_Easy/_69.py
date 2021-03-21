from typing import List
import math 
class Solution:
    def mySqrt(self, x: int) -> int:
        print(int(math.sqrt(x)))
        return int(math.sqrt(x))

slt = Solution()    
# Test Case
slt.mySqrt(8)

"""
69. Sqrt(x)

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, 
and only the integer part of the result is returned.

Example 1:
    Input: x = 4
    Output: 2

Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

Constraints:
    0 <= x <= 231 - 1
"""
