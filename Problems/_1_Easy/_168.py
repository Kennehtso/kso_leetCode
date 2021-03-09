from typing import List
class Solution:
      def convertToTitle(self, columnNumber: int) -> str:
          ans = ''
          while columnNumber > 0:
              minus1 = columnNumber - 1
              ans = chr( minus1 % 26 + 65) + ans
              columnNumber = minus1 // 26
          print(ans)
          return ans

slt = Solution()    
# Test Case
slt.convertToTitle(701)
slt.convertToTitle(2147483647)

"""168. Excel Sheet Column Title
For example:
  A -> 1
  B -> 2
  C -> 3
  ...
  Z -> 26
  AA -> 27
  AB -> 28 
  ...
Example 1:
  Input: columnNumber = 1
  Output: "A"

Example 2:
  Input: columnNumber = 28
  Output: "AB"

Example 3:
  Input: columnNumber = 701
  Output: "ZY"

Example 4:
  Input: columnNumber = 2147483647
  Output: "FXSHRXW"
"""
