from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        half, r = 0, 0
        for k, v in Counter(s).items():
            half += v // 2
            if r == 0 and v % 2 !=0 : r = 1    
        ans = half * 2 + r
        print(ans)        
        return ans

slt = Solution()
# Test Case
slt.longestPalindrome("abccccdd")
slt.longestPalindrome("a")
slt.longestPalindrome("ab")
slt.longestPalindrome("Aa")
slt.longestPalindrome("AAAA")
"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
    Input: s = "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
    Input: s = "a"
    Output: 1
    Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.
""" 