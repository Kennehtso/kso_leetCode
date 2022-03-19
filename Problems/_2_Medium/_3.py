from typing import List
class Solution:
    isDebug = True
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        fifo, mx = [], 0
        for _s in s:  
            if _s in fifo:
                if len(fifo) > mx:
                    mx = len(fifo) 
                del fifo[0:fifo.index(_s)+1]
            fifo.append(_s)

        if len(fifo) > mx:
            mx = len(fifo) 

        if self.isDebug: print(fifo," : ",mx)
        return mx

    def lengthOfLongestSubstring_20220310(self, s: str) -> int:
        cur, m = '', 0
        for c in s:
            if c not in cur:
                cur += c
                m = max(m, len(cur))
            else:
                m = max(m,len(cur))
                cur = cur[cur.index(c)+1::] + c
        if self.isDebug: print(cur," : ",m)
        return m

slt = Solution()    
# Test Case
slt.lengthOfLongestSubstring(s = "abccdeddakgjazfyrasfdhwqfcrqaxzfwcaxzrw")
slt.lengthOfLongestSubstring_20220310(s = "abccdeddakgjazfyrasfdhwqfcrqaxzfwcaxzrw")

"""
3. Longest Substring Without Repeating Characters
Medium

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

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.


"""
