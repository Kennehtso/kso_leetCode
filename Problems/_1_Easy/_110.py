from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root: return 0
            left_h = helper(root.left)
            right_h = helper(root.right)
            if left_h is None or right_h is None or abs(left_h-right_h) > 1:
                return None
            return max(left_h, right_h) + 1
        if not root: return True
        return helper(root)
        """
                                        1
                        2                               2
                3               3       
            4       4       
         """
slt = Solution()

_8 = TreeNode(8,None,None)
_7 = TreeNode(7,None,_8)
_6 = TreeNode(6,None,None)
_4 = TreeNode(4,_6,_7)
_5 = TreeNode(5,None,None)
_3 = TreeNode(3,None,None)
_2 = TreeNode(2,_4,_5)
_root = TreeNode(1,_2,_3)
slt.isBalanced(_root)

"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: true

Example 2:
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false

Example 3:
    Input: root = []
    Output: true


Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -104 <= Node.val <= 104

"""
