from typing import List
class Solution:
    def isOverLap(self, meetings)->bool:
        pre = (0,0)
        print(meetings)
        meetings.sort()
        print(meetings)
        for idx in range(1, len(meetings)):
            if meetings[idx-1][1] > meetings[idx][0]:
                return False
        return True
slt = Solution()
m1 = [(15, 20), (5, 10), (10,13), (0, 20), (0,30)]
m2 = [(0, 10), (20, 30), (10,21)]
m3 = [(0, 10), (20, 30), (10,20)]
m4 = [(20,25), (15, 20), (0,10)]
m5 = [(20,30), (0,10)]
print(slt.isOverLap(m1)) # False
print(slt.isOverLap(m2)) # False
print(slt.isOverLap(m3)) # True
print(slt.isOverLap(m4)) # True
print(slt.isOverLap(m5)) # True
"""
920. Meeting Room

Check if a person can participate all meeting without overlap 

Example 1:
    Input: p = [(0,30), (5, 10), (15, 25)]
    Output: false
"""
