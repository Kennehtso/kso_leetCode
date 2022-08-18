from typing import List
class Solution:    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #print("==================================")
        #print("newInterval: %s"%(newInterval))
        idx = 0
        while idx < len(intervals):
            #print(intervals)
            #print(idx)
            # new not overlap
            if not(newInterval[1] < intervals[idx][0] or newInterval[0] > intervals[idx][1]):
                start = min(intervals[idx][0], newInterval[0])
                end = max(intervals[idx][1], newInterval[1])
                newInterval = [start, end]
                intervals.pop(idx)
                idx -= 1
            idx += 1
        intervals.append(newInterval)
        intervals.sort()
        #print("finals :",intervals)
        return intervals

slt = Solution()    
# Test Case
slt.insert("ASD SADSAFSASAD ASSAD ")
"""
58. Length of Last Word

Given a string s consists of some words separated by spaces, 
return the length of the last word in the string. 
If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only.

Example 1:
    Input: s = "Hello World"
    Output: 5

Example 2:
    Input: s = " "
    Output: 0

Constraints:
    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
"""
