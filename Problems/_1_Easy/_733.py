from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image, self.newColor, self.targetColor, self.row_max, self.col_max, self.chkArr = image, newColor, image[sr][sc], len(image), len(image[0]), []
        print(self.image)
        self.updateColor(sr, sc)
        print(self.image)
        return self.image
    
    def updateColor(self, sr, sc):
        self.chkArr.append((sr, sc))
        self.image[sr][sc] = self.newColor
        e, s, w, n = (sr, sc+1), (sr+1, sc), (sr, sc-1), (sr-1, sc)
        if e not in self.chkArr and self.image[e[0]][e[1]] != self.newColor and self.image[e[0]][e[1]] == self.targetColor and e[0] < self.row_max and e[1] < self.col_max :
            self.updateColor(e[0], e[1])

        if s not in self.chkArr and self.image[s[0]][s[1]] != self.newColor and self.image[s[0]][s[1]] == self.targetColor and s[0] < self.row_max and s[1] < self.col_max :
            self.updateColor(s[0], s[1])
                
        if w not in self.chkArr and self.image[w[0]][w[1]] != self.newColor and self.image[w[0]][w[1]] == self.targetColor and w[1] >=0 and w[0] < self.row_max and w[1] < self.col_max :
            self.updateColor(w[0], w[1])
                
        if n not in self.chkArr and self.image[n[0]][n[1]] != self.newColor and self.image[n[0]][n[1]] == self.targetColor and n[0] >=0 and n[0] < self.row_max and n[1] < self.col_max :
            self.updateColor(n[0], n[1])
        
slt = Solution()    
# Test Case
slt.floodFill([[0,0,0],[0,1,1]],1,1,1)
slt.floodFill([[5,5,5,2,2],[2,2,5,3,3],[4,4,5,5,5],[5,5,5,5,5],[0,0,0,0,0]],3,2,9)

"""
733. Flood Fill

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, 
and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, 
plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), 
and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
  image = [[1,1,1],[1,1,0],[1,0,1]]
  sr = 1, sc = 1, newColor = 2
Output: 
  [[2,2,2],[2,2,0],[2,0,1]]

Explanation: 
  From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
  by a path of the same color as the starting pixel are colored with the new color.
  Note the bottom corner is not colored 2, because it is not 4-directionally connected
  to the starting pixel.

Note:
  The length of image and image[0] will be in the range [1, 50].
  The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
  The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""
