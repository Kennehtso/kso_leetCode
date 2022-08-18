from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, d = 0, ''
        for c in s:
            if c not in d:
                d += c
                continue
            if ans < len(d): ans = len(d)
            d = d[d.index(c)+1:] + c
        return len(d) if ans < len(d) else ans
    
slt = Solution()    
# Test Case
slt.lengthOfLongestSubstring("")
slt.lengthOfLongestSubstring("pwwkew")
"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
    Input: s = ""
    Output: 0


Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.


"""
