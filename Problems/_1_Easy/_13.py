from typing import List
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    #'MMCMLXXIX'
    def romanToInt(self, s: str) -> int:
        # Note:
            # len(s) = 9
            # range(9 -1) = range(8) = [0, 1, 2, 3, 4, 5, 6, 7,]
            # reversed(range(len(s) - 1)) = reversed([0, 1, 2, 3, 4, 5, 6, 7]) = 7, 6, 5, 4, 3, 2, 1, 0]
        # Key :
            # s[8] is here as init for total
            # loop index start from 7, s[7], compare with s[index + 1], which mean the previous one
                # if current < previous, total minus current value
                # else (if current >= previous), total add current value
        total = values.get(s[-1]) 
        for i in reversed(range(len(s) - 1)):
            _cur = values[s[i]]
            _pre = values[s[i + 1]]
            if _cur < _pre:
                total -= _cur
            else:
                total += _cur
        return total
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

"""
slt = Solution()
# Test Case
slt.romanToInt("MMCMLXXIX")
