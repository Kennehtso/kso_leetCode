from typing import List
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        chkList =  list(s)
        r, r_2d = '', [[""] * (len(s)//2 if len(s) % numRows >numRows else len(s)) for i in range(numRows)]
        #print(r_2d)
        col_start_pos, row_pos = 0, 0
        while chkList:
            if row_pos < numRows:
                if not chkList: break
                #print(F"r_2d[{row_pos}][{col_start_pos}] : {chkList[0]}")
                r_2d[row_pos][col_start_pos] = chkList.pop(0)
                row_pos +=1
                #print("Move By Row\n"+str(chkList)+"\n---------------")
            else:
                for backwardIdx in range(numRows -2 , 0,-1):
                    if not chkList: break
                    col_start_pos +=1 
                    #print(F"r_2d[{backwardIdx}][{col_start_pos}] : {chkList[0]}")
                    r_2d[backwardIdx][col_start_pos] = chkList.pop(0)
                    #print("Move By Col \n"+str(chkList)+"\n---------------")
                row_pos = 0 # reset For the next
                col_start_pos += 1
        for idx in range(0, numRows):
            print(r_2d[idx])
            r+= "".join(r_2d[idx])
        #print(r)
        return r

slt = Solution()    
# Test Case
slt.convert(digits = [4,3,2,1])

"""
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

 
Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

Example 3:
    Input: s = "A", numRows = 1
    Output: "A"

Constraints:
    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000

"""
