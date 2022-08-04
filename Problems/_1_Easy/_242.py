from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def helper(s):
            s = s.lower()
            res = {}
            for c in s:
                if c in res:
                    res[c] += 1
                else:
                    res[c] = 1
            return res
        return helper(s) == helper(t)
slt = Solution()    
# Test Case

slt.isAnagram(s ="anagram", t = "nagaram")

"""
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false
Note:
    You may assume the string contains only lowercase alphabets.

Follow up:
    What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
