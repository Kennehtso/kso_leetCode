from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Do not allocate extra space for another array, 
        # you must do this by modifying the input array in-place with O(1) extra memory.
        s.reverse()
        """ l = len(s)
        for idx in range(0, l):
            s.insert(idx,s.pop(l-1)) """
            
slt = Solution()
# Test Case
slt.reverseString(["h","e","l","l","o"])
"""
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10

Example 2:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101

Constraints:
    0 <= n <= 105

Follow up:
    It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
    Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?


"""