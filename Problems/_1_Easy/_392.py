from typing import List
class Solution:
     def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        d, t_arr = {}, [(v, idx) for idx, v in enumerate(t)]
        #print(t_arr)
        p = list(filter(lambda e: e[0] is s[0] , t_arr))
        if not p: return False
        d[s[0]] = p
        pre = d[s[0]].pop(0)
        for idx in range(1, len(s)):
            mx = list(filter(lambda e: e[0] is s[idx] , t_arr))
            if s[idx] not in d:
                d[s[idx]] = mx
            if not mx or not d[s[idx]]:
                return False
            m = d[s[idx]].pop(0)
            while d[s[idx]] and m[1] <= pre[1]:
                m = d[s[idx]].pop(0)
            if m[1] < pre[1]:
                return False
            pre = m
        return True
        """ if not s: return True
        max_i, t_arr = [], [(v, idx) for idx, v in enumerate(t)]
        #print(t_arr)
        p = list(filter(lambda e: e[0] is s[0] , t_arr))
        if not p: return False
        pre = p[0]
        max_i.append(pre)
        for idx in range(1, len(s)):
            mx = list(filter(lambda e: e[0] is s[idx] , t_arr))
            #print(mx)
            if not mx:
                return False
            m = mx[0]
            for idx in range(1, len(mx)):
                if mx[idx] not in max_i:
                    m = mx[idx]
                    break
            
            if m[1] - pre[1] < 1:
                return False
            pre = m
            max_i.append(m)
        #print(max_i)
        return True
         """

slt = Solution()
slt.isSubsequence("bb","ahbgdc")

"""
392. Is Subsequence

Given two strings s and t, check if s is a subsequence of t.

A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 
Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false


Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.

"""
