# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right

class Solution:
    r = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def gogo(root: TreeNode, locateMsg):
            #print(locateMsg+" **************")
            if root is None:
                return 0
            left = gogo(root.left, f"Going Left of {root.val}")
            #print(f"left: {left}")
            right = gogo(root.right,  f"Going Right of {root.val}")
            #print(f"right: {right}")
            self.r = max(self.r,left+right+1)
            #print(f"max - self.r: {self.r}")
            return max(left, right) + 1

        gogo(root,"ROOT")
        #print(f"self.r: {self.r-1}")
        return self.r - 1 if self.r > 0 else 0

slt = Solution()
# Test Case
#result = slt.longestCommonPrefix(["dog","racecar","car"])
_8 = TreeNode(8,None,None)
_7 = TreeNode(7,None,_8)
_6 = TreeNode(6,None,None)
_4 = TreeNode(4,_6,_7)
_5 = TreeNode(5,None,None)
_3 = TreeNode(3,None,None)
_2 = TreeNode(2,_4,_5)
_root = TreeNode(1,_2,_3)

slt.diameterOfBinaryTree(_root)

"""
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""