from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is '':
            return True
        abc = "".join(filter(str.isalnum, s)).lower()
        print(abc == abc[::-1])
        return abc == abc[::-1]

slt = Solution()    
# Test Case
slt.isPalindrome("A man, a plan, a canal: Panama")
"""
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
    Input: "A man, a plan, a canal: Panama"
    Output: true

Example 2:
    Input: "race a car"
    Output: false

Constraints:
    s consists only of printable ASCII characters.


"""
