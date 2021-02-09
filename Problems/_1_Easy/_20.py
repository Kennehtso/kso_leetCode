from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        # Stack
        if len(s) == 1:
            return False
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                    stack.pop()
            else:
                print(False)
                return False
        
        print(stack == [])
        return stack == []
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