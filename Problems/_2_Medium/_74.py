from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right, n = 0, len(matrix)-1, len(matrix[0])-1
        while left <= right:
            #print("matrix: %s"%(matrix))
            mid = ( left + right) // 2
            #print("cur matrix: %s"%(matrix[mid]))
            if target in matrix[mid]:
                return True
            elif  matrix[mid][n] < target:
                left = mid + 1
            else:
                right = mid - 1
            #print('--')
        return False
        


slt = Solution()    
# Test Case
slt.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)

"""
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 
Example 1:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

Example 2:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false


Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104rget <= 109

"""