from typing import List
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs)
        if l == 1: return strs[0]
        prefix = strs[0]
        for i in range(1, l):
            cur = strs[i]
            while prefix > cur or cur.find(prefix) != 0:
                prefix = prefix[:len(prefix)-1]
            if not prefix: return ""
        return prefix

    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = ""
        for tur in zip(*strs):
            if len(set(tur)) > 1: break
            r += tur[0]
        return r
        """
        
slt = Solution()
# Test Case
#result = slt.longestCommonPrefix(["dog","racecar","car"])
result = slt.longestCommonPrefix(["flower","flow","flight"])


"""
14. Longest Common 

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
 
Constraints:
    0 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
"""