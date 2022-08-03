from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        s = s.lower()
        while start < end:
            while start < end:
                if  s[start].isalnum():
                    break
                start += 1
            while start < end:
                if s[end].isalnum():
                    break
                end -= 1
            if s[start] != s[end]: return False
            start += 1
            end -= 1
        return True

    def isPalindrome2(self, s: str) -> bool:
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
