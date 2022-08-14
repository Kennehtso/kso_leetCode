from re import X
from typing import List
class Solution:
    def isPalindrome(self, x: int) -> bool:
        val, rev, stk = x, 0, []
        while val > 0:
            stk.append(val % 10)
            val = val // 10
        #print(stk)
        level = 1
        while stk:
            rev += (stk.pop() * level)
            level *= 10
        #print("%s vs %s = "%(rev, x))
        return rev == X
"""
datetime : 09/06/2020 15:47
Follow up: Could you solve it without converting the integer to a string?
       ## No String.. 
        
        if x==0 :
            return True
        elif x <0 or x % 10== 0 :
            return False
        count = 0
        countTarget = x
        while( countTarget > 0 ):
            countTarget = countTarget//10
            count = count + 1
        if x == 0  and count == 1:
            return True
        
        isNotZero = True
        decDigit = 10
        minusTarget = 0
        decimalList = []
        target = x
        while isNotZero :
            chk = target / decDigit
            if chk > 0.1:
                modDigit = target % decDigit - minusTarget
                minusTarget += modDigit
                decimalList.append(int(modDigit / (decDigit/10)))
                decDigit*=10
            else:
                isNotZero = False
        
        if decimalList == list(reversed(decimalList)) :
            return True
           # print('Is a Palindrome Number')
        else:
            return False
           # print('Is not a Palindrome Number ','\n','Orginal: ', decimalList, '\n', 'New: ', list(reversed(decimalList)))
            
        
"""
"""
9. Palindrome Number
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
-2^31 <= x <= 2^31 - 1
"""
slt = Solution()
# Test Case
result = slt.isPalindrome(1233454321)
result = slt.isPalindrome(123454321)
result = slt.isPalindrome(-123)
result = slt.isPalindrome(0)
result = slt.isPalindrome(-1234234324321)
result = slt.isPalindrome(1234234324321)
