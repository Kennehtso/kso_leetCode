from typing import List
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        while S.count("#") > 0:
            S = S[0:S.index("#") if S.index("#")-1 < 0 else S.index("#")-1] + S[S.index("#")+1::]
        while T.count("#") > 0:
            T = T[0:T.index("#") if T.index("#")-1 < 0 else T.index("#")-1] + T[T.index("#")+1::]
        return S == T

slt = Solution()    
# Test Case
slt.backspaceCompare(S = "a##c", T = "#a#c")
"""
844. Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".

Example 2:
    Input: S = "ab##", T = "c#d#"
    Output: true
    Explanation: Both S and T become "".

Example 3:
    Input: S = "a##c", T = "#a#c"
    Output: true
    Explanation: Both S and T become "c".

Example 4:
    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".

Note:
    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:
    Can you solve it in O(N) time and O(1) space?

"""
