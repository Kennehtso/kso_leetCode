from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r, m = "", min(strs)
        for idx in range(0, len(m)):
            hasDiff = any(s[idx] != m[idx] for s in strs)
            if not hasDiff:
                r += m[idx]
            else:
                break
        print(r)
        return r

slt = Solution()
# Test Case
result = slt.longestCommonPrefix(["dog","racecar","car"])
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