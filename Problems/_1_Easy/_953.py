from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pre = words[0]
        passFlag = True
        print(f'------------ Check For: {words}-------------')
        for idx in range(1, len(words)):
            cur = words[idx]
            roundCheck, isMatch = False, False
            subtractList = list(map(lambda x, y: order.index(x) - order.index(y) , pre, cur)) 
            if sum(subtractList) == 0:
                isMatch = True
            else:
                for idx, substract in enumerate(subtractList):
                    if substract > 0:
                        break
                    elif substract < 0:
                        roundCheck = True
                        break
            if isMatch and (len(pre) <= len(cur)) :
                roundCheck = True
                
            print(f'Verify -> pre: "{pre}" , cur: "{cur}" \nResult: {roundCheck}')
            if not roundCheck:
                passFlag = roundCheck
                break
            pre = cur
        print('------------ END -------------')
        return passFlag
slt = Solution()
# Test Case
slt.isAlienSorted(["zirqhpfscx","zrmvtxgelh","vokopzrtc","nugfyso","rzdmvyf","vhvqzkfqis","dvbkppw","ttfwryy","dodpbbkp","akycwwcdog"],
"khjzlicrmunogwbpqdetasyfvx")
#slt.isAlienSorted(words=["word","world","row"], order = "worldabcefghijkmnpqstuvxyz")
#slt.isAlienSorted(words=["app","apple"], order = "abcdefghijklmnopqrstuvwxyz")
#slt.isAlienSorted(words=["l","h"], order = "xkbwnqozvterhpjifgualycmds")
#slt.isAlienSorted(words=["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")
#slt.isAlienSorted(words=["word","world","row"], order = "worldabcefghijkmnpqstuvxyz")
#slt.isAlienSorted(words=["apple","app"], order = "abcdefghijklmnopqrstuvwxyz")
"""
953. Verifying an Alien Dictionary
In an alien language, surprisingly they also use english lowercase letters, 
but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographicaly in this alien language.
================================================================================================================
Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, 
and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", 
because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

================================================================================================================

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.

"""
