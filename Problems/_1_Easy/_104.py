from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0 
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
            
slt = Solution()
#True
_8 = TreeNode(8,None,None)
_7 = TreeNode(7,None,_8)
_6 = TreeNode(6,None,None)
_4 = TreeNode(4,_6,_7)
_5 = TreeNode(5,None,None)
_3 = TreeNode(3,None,None)
_2 = TreeNode(2,_4,_5)
_root = TreeNode(1,_2,_3)
slt.maxDepth(_root)
"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input: root = [1,null,2]
    Output: 2

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100

"""