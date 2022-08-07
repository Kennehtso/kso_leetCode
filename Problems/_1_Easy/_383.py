from typing import List
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d_m = {}
        for s in magazine:
            if s not in d_m: d_m[s] = 0
            d_m[s] += 1
        for s in ransomNote:
            if s not in d_m or d_m[s] == 0:
                print(False)
                return False
            d_m[s] -= 1
        print(True)
        return True

        
#1 , (2, (3, (4, (5, (4, (3, (2, (1, None))))))))
slt = Solution()
slt.canConstruct("a","a")
slt.canConstruct("a","b")
slt.canConstruct("az","a")
slt.canConstruct("a","az")
slt.canConstruct("aa","a")
slt.canConstruct("a","aa")
slt.canConstruct("aabbaaca", "abccaca")
slt.canConstruct("aa","bbaa")
slt.canConstruct("bbaa","aa")
slt.canConstruct("aaz","bb")

"""
383. Ransom Note

Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true
"""

