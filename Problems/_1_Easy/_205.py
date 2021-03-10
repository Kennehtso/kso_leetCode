from typing import List
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sTotMap, tTosMap = {},{}
        for idx in range(0,len(s)):
            if s[idx] not in sTotMap :
                sTotMap[s[idx]] = t[idx]
                #print(f"add s: {s[idx]}")
                if t[idx] in tTosMap and tTosMap[t[idx]] is not s[idx]:
                    return False
                elif t[idx] not in tTosMap :
                    tTosMap[t[idx]] = s[idx]
                    print(f"add t: {t[idx]}")
            elif sTotMap[s[idx]] is not t[idx]:
                return False
            """
            print(f"sTotMap: {sTotMap}")
            print(f"tTosMap: {tTosMap}")
            print(f"-----")
            """ 
        return True
        
slt = Solution()    
# Test Case
slt.isIsomorphic(s = "paper", t = "title")

"""205. Isomorphic Strings
Easy

1893

456

Add to List

Share
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:
    Input: s = "egg", t = "add"
    Output: true

Example 2:
    Input: s = "foo", t = "bar"
    Output: false

Example 3:
    Input: s = "paper", t = "title"
    Output: true
 

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
