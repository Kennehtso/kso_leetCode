from typing import List
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            if c in d:
                d[c] = -1
            else:
                d[c] = i
        r = list(filter(lambda e: e>-1, d.values()))
        if len(r) > 0:
            print(r[0])
            return r[0]
        print(-1)
        return -1
        
            
        
#1 , (2, (3, (4, (5, (4, (3, (2, (1, None))))))))
slt = Solution()
slt.firstUniqChar("leetcode")
slt.firstUniqChar("loveleetcode")
slt.firstUniqChar("abcdefghiabcdefghi")

"""
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:
    s = "leetcode"
    return 0.

    s = "loveleetcode"
    return 2.
 
Note: 
    You may assume the string contains only lowercase English letters.
"""
