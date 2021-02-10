from typing import List
class Solution:
    def romanToInt(self, input_roman: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        # M M C M L X X I X 
        total = 0
        position = 0
        s_len = len(input_roman)
        while position < s_len:
            # If this is the subtractive case.
            current_value = values [ input_roman[position] ]
            next_value = values [ input_roman[position + 1] ]
            if  current_value < next_value :
                total = total + ( next_value - current_value)
                position  = position + 2
            # Else this is NOT the subtractive case.
            else:
                total = total + current_value
                position = position + 1
        return total

    def rev_romanToInt(self, input_roman: str) -> int:
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        if len(s) == 1:return d[s]
        r = pre = d[s[-1]]
        for idx in range(len(s)-2,-1,-1):
            cur = d[s[idx]]
            r += cur * (1 if cur >= pre else -1) 
            pre = cur
        return r

slt = Solution()
slt.rev_romanToInt("MMCMLXXIX")

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