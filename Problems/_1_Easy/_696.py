from typing import List
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre, count, lastOppositeIdx = s[0], 0, -1
        for idx in range(1, len(s)):
            if pre != s[idx]:
                count +=1
                lastOppositeIdx = idx -1
            elif lastOppositeIdx > 0 and s[lastOppositeIdx-1] == s[lastOppositeIdx]:
                count +=1
                lastOppositeIdx -=1
            pre = s[idx]
        return count
           
        
slt = Solution()
# Test Case
#result = slt.longestCommonPrefix(["dog","racecar","car"])
slt.countBinarySubstrings("100111001")


"""
696. Count Binary Substrings

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.

Example 1:
    Input: "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
    Notice that some of these substrings repeat and are counted the number of times they occur.
    Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
    Input: "10101"
    Output: 4
    Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:
    s.length will be between 1 and 50,000.
    s will only consist of "0" or "1" characters.
"""