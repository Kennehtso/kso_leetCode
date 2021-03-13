from typing import List  
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            print(True)
            return True
        intervals.sort()
        lTime, mTime = intervals[0][0], intervals[0][1]
        for idx in range(1,len(intervals)):
            if lTime < intervals[idx][1] < mTime  or lTime < intervals[idx][0] < mTime :
                print(False)
                return False
            lTime = min(lTime, intervals[idx][0])
            mTime = max(mTime, intervals[idx][1])
        print(True)
        return True

slt = Solution()    
# Test Case
l = [[0,30],[5,10],[15,20]]
slt.canAttendMeetings(l)
l = [[7,10],[2,4]]
slt.canAttendMeetings(l)

"""
252. Meeting Rooms

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: false

Example 2:
    Input: intervals = [[7,10],[2,4]]
    Output: true
 
Constraints:
    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti < endi <= 106
"""
