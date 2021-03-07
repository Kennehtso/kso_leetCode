from typing import List
class Solution:
    def removeDuplicates(self, S: str) -> str:
        hasDuplcate = True
        while hasDuplcate:
            if len(S) == 0:
                break
            pre = S[-1]
            hasDuplcate = False
            for idx in range(len(S)-2, -1, -1):
                cur = S[idx]
                if pre == cur:
                    S = S[:idx] + S[idx+2:]
                    hasDuplcate = True
                    pre = ''
                else:
                    pre = cur
        return S
    """ hasDuplcate, result = True, ""
    def removeDuplicates(self, S: str) -> str:
        if len(S) == 0:
            return S
        pre = S[-1]
        self.hasDuplcate = False
        for idx in range(len(S)-2, -1, -1):
            cur = S[idx]
            if pre == cur:
                S = S[:idx] + S[idx+2:]
                self.hasDuplcate = True
                pre = ''
            else:
                pre = cur
        if self.hasDuplcate:
            self.removeDuplicates(S)
        
        self.result = S if self.result =="" else self.result
        return self.result """



slt = Solution()
#slt.removeDuplicates("abbaca")
expect = "pjoefymphlowpdlaltrqsbfyfgfjuopfsdmitlrnrehdvpjfxexgcuasysrxpiarijesfkyuegrahmbkbvgovcbfkgjlifufogxljhlsbhafhrolpufsusqutxutbjnfdlykcmubsnlgvrqvrwnrvxnieolmsplqdpdrdohanjateujfdkbtswkxdvbqvofvkmcwouyxvaxprgdcsprflsfcgvxuvqhaohnvilhkcpbfoicjtxytcmrvwchvsrverfmakcrjdavcopshpsqcqbgvswgrwdtpuaiexhpoqwtirvysnjruixnjqjbaevawqoicnimifspayfdntkivjxlhvlaeorgqoxrsvfsgwepgrimbvgloykdbjqsdvjfbklengcawpytmqvwmurgaexngmumqtychfpvplqxfjercrwrwrwnhtyndmfthrkfkhmhspuqfmhqgybknuhmxhuwbsmehpjoefymphlowpdlaltrqsbfyfgfjuopfsdmitlrnrehdvpjfxexgcuasysrxpiarijesfkyuegrahmbkbvgovcbfkgjlifufogxljhlsbhafhrolpufsusqutxutbjnfdlykcmubsnlgvrqvrwnrvxnieolmsplqdpdrdohanjateujfdkbtswkxdvbqvofvkmcwouyxvaxprgdcsprflsfcgvxuvqhaohnvilhkcpbfoicjtxytcmrvwchvsrverfmakcrjdavcopshpsqcqbgvswgrwdtpuaiexhpoqwtirvysnjruixnjqjbaevawqoicnimifspayfdntkivjxlhvlaeorgqoxrsvfsgwepgrimbvgloykdbjqsdvjfbklengcawpytmqvwmurgaexngmumqtychfpvplqxfjercrwrwrwnhtyndmfthrkfkhmhspuqfmhqgybknuhmxhuwbsmeh"
result = slt.removeDuplicates("pjoefymphlowpdlaltrqsbfeeffyfnngfjuopfxxsdmitlrnrehdvpjfxexgcuhhasysrxpiarijesfkyuegrahmbkbvgovcbfkgjlifufogxljhlsbhafhrolpufsusqutxutbjnjjfdlykcmubsnlgvrqvrwnrnnvxnieolmsplqdpdrdohanjateujfdkbtswkxdggvbqvofvkmcwouyxvaxprgdcsprflsjjfcgvxuvqhaohnvilhkcpbfoicjtxytcmrvwchvsrverfmakcrjdavcopshpsqcqbgvswgrwdtpuaffiexhpoqwtirvysnjruixnjqjbaevammwqoicnimifspayfdntkivjttxpplllhvlaeorgqoxrsvfsgwepgrimbvgloykdbjqsdvjfbklengcawpytmqvwmurgaexngmumqtychfpvplqxfjercggrbbwrwrwnhtyndmfthrkfkhmhspuqkkfmhqgyllbknuhmxhuwbsmehpjoefymphlowpdlaltrqsbfeeffyfnngfjuopfxxsdmitlrnrehdvpjfxexgcuhhasysrxpiarijesfkyuegrahmbkbvgovcbfkgjlifufogxljhlsbhafhrolpufsusqutxutbjnjjfdlykcmubsnlgvrqvrwnrnnvxnieolmsplqdpdrdohanjateujfdkbtswkxdggvbqvofvkmcwouyxvaxprgdcsprflsjjfcgvxuvqhaohnvilhkcpbfoicjtxytcmrvwchvsrverfmakcrjdavcopshpsqcqbgvswgrwdtpuaffiexhpoqwtirvysnjruixnjqjbaevammwqoicnimifspayfdntkivjttxpplllhvlaeorgqoxrsvfsgwepgrimbvgloykdbjqsdvjfbklengcawpytmqvwmurgaexngmumqtychfpvplqxfjercggrbbwrwrwnhtyndmfthrkfkhmhspuqkkfmhqgyllbknuhmxhuwbsmeh")
print("Same" if expect == result else "Not as Expect")

slt = Solution()
expect = "ca"
result = slt.removeDuplicates("abbaca")
print(f"expect, result: {expect}:{result}")
print("Same" if expect == result else "Not as Expect")

"""
1047. Remove All Adjacent Duplicates In String

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:
    Input: "abbaca"
    Output: "ca"
    Explanation: 
    For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
    and this is the only possible move.  The result of this move is that the string is "aaca",
    of which only "aa" is possible, so the final string is "ca".
    

Note:
    1 <= S.length <= 20000
    S consists only of English lowercase letters.
"""