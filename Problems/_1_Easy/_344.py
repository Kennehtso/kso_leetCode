from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Do not allocate extra space for another array, 
        # you must do this by modifying the input array in-place with O(1) extra memory.
        l = len(s)
        for idx in range(0, l):
            s.insert(idx,s.pop(l-1))
            print(s)
        print("Done")
        print(s)
            
slt = Solution()
# Test Case
slt.reverseString(["h","e","l","l","o"])
"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:
    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

"""