from typing import List
"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
-2
-2+1
"""
class Solution:
      def addStrings(self, num1: str, num2: str) -> str:
            d={ "0":0, "1":1, "2":2, "3":3, "4":4,  "5":5,  "6":6, "7":7,  "8":8, "9":9 }
            num1, num2 = num1[::-1], num2[::-1]
            a, r =0, "" 
            for idx in range(max(len(num1), len(num2))+1):
                isOverNum1 = idx >= len(num1)
                isOverNum2 = idx >= len(num2)
                num1_cur = 0 if isOverNum1 else d[num1[idx]]
                num2_cur = 0 if isOverNum2 else d[num2[idx]]
                s, s_cal = (num1_cur + num2_cur + a), 0
                if s == 0 and isOverNum1 and isOverNum2:
                    break
                elif s < 10:
                    s_cal = s
                    a = 0
                else:
                    s_cal =  s - 10
                    a = 1
                r =  str(s_cal) + r
            print(r)
            return r if len(r) > 0 else "0"
slt = Solution()
# Test Case
slt.addStrings("501","6")
slt.addStrings("152832","3359")

"""
415. Add Strings
    Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
""" 