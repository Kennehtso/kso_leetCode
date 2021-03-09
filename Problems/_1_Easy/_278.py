from typing import List
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    firstBadVer = 0
    def isBadVersion(self, bad):
        return bad > self.firstBadVer

    def firstBadVersion(self, n, bad):
        print(f"max: {n}, bad: {bad}")
        self.firstBadVer = bad #This is the condition, cant compare it directly
        left,right = 1,n
        while left < right:
            mid = left + (right-left)/2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid +1
            print(f"left: {left}, right: {right}")
        print(int(left))
        return int(left)
        
            
slt = Solution()
# Test Case
slt.firstBadVersion(300, 15)
"""
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
    Input: n = 5, bad = 4
    Output: 4
    Explanation:
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    Then 4 is the first bad version.

Example 2:
    Input: n = 1, bad = 1
    Output: 1


Constraints:
    1 <= bad <= n <= 231 - 1

"""