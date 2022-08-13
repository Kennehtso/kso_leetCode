from typing import List
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, add = '', False
        d_s = {0:"0",1:"1",2:"0",3:"1"}
        d_flag = {0:False,1:False,2:True,3:True}
        def helper(s):
            s_n = s[-1]
            return 1 if s_n == "1" else 0, s[:len(s)-1]
        while a != '' and b != '':
            v_a, n_a = helper(a)
            v_b, n_b = helper(b)
            a = n_a
            b = n_b
            r = add + v_a + v_b
            add = d_flag[r]
            res = d_s[r] + res
        while a!='':
            v_a, n_a = helper(a)
            a = n_a
            r = add + v_a 
            add = d_flag[r]
            res = d_s[r] + res
        while b!='':
            v_b, n_b = helper(b)
            b = n_b
            r =  add + v_b
            add = d_flag[r]
            res = d_s[r] + res
        return "1" + res if add else res
        """
    def addBinary(self, a: str, b: str) -> str:
        ans = bin(int(a,2)+int(b,2))
        return ans[2:len(ans)]
    """
slt = Solution()    
# Test Case
slt.addBinary(a = "1010", b = "1011")

"""
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.


Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"
 

Constraints:
    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
"""
