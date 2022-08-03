from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stk, mapper = [], {")":"(", "}":"{","]":"["}
        for c in s:
            if stk and c in mapper and mapper[c] == stk[-1] :
                stk.pop()
                continue
            stk.append(c)
        return not stk
    """
    def isValid(self, s: str) -> bool:
        r = True
        if s.count("{") != s.count("}") or s.count("[") != s.count("]") or s.count("(") != s.count(")") or len(s) == 1 :
            print(False)   
            return not r
        d_open, d_close= {"(":")", "[":"]","{":"}"}, {")":"(","]":"[","}":"{"}
        chkList, searchOpenTarget = [], []
        for idx in range(len(s)):
            cur = s[idx]
            chkList.append(idx)
            if cur in d_close:
                searchOpenTarget.append(d_close[cur])
                chkList.remove(idx)
                for chkItem in range(len(chkList)-1, -1,-1):
                    idx_sub = chkList[chkItem]
                    chkList.remove(idx_sub)
                    cur_back = s[idx_sub]
                    if cur_back in d_open:
                        if cur_back == searchOpenTarget[-1]:
                            searchOpenTarget.pop()
                            break
                        else: # invalid
                            r = False
                            break 
                    elif cur_back in d_close:
                        searchOpenTarget.append(cur_back)
                if len(searchOpenTarget) != 0:
                    r = False
                if r is False:
                    break
        print(r)       
        return r
    """
slt = Solution()
# Test Case
#slt.isValid("(){}}{")
#slt.isValid("()")
slt.isValid("([]{[()]})[]")
slt.isValid("([]{()]})[]")
#slt.isValid("([])")
# stop in first close
# look for the match open eg: '[' 
# foreach back:
# 1. if meet a close, search for this match of open first
# 2. if meet a open 
#   2.1 - that not match, return false
#   2.2 - that match, save the index that will 'continue' next time reverse searching.

# ({{([({{()}})])}})


"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
 
Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.
""" 