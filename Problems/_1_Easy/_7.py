from typing import List
class Solution:
    def reverse(self, x: int) -> int:
        max = pow(2,31)
        if x == 0 :
            #print(0)
            return 0
        else:
            sign = 1 if x > 0 else -1
            x *= sign
            l = list(str(x))
            l.reverse()
            #print(int(s)*sign)
            r = int("".join(l)) * sign
            if  max < r or r < (-1 * max) : return 0
            return r
"""
datetime : 09/06/2020 15:47
    negativeSwitch = -1
        if x > 0:
            negativeSwitch = 1
            
        trans = x * negativeSwitch
        revLisrt = reversed(list(map(str,str(trans))))
        revJoin = "".join(revLisrt)
        target = int(revJoin) * negativeSwitch
        if pow(2,31) *-1 > target or target > pow(2,31)-1 :
            return 0
        return target
"""
"""
7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Constraints:
 -2^31 <= x <= 2^31 - 1
"""
slt = Solution()
# Test Case
result = slt.reverse(1534236469)
result = slt.reverse(-123)
result = slt.reverse(-34453454234)
result = slt.reverse(-899834546765)
result = slt.reverse(51235324123415756)