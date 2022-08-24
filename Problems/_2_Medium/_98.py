from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root, left_v, right_v):
            # Base
            if not root: 
                return True
            # Normal
            elif not(left_v < root.val < right_v): 
                return False
            # dfs
            return dfs(root.left, left_v, root.val) and dfs(root.right, root.val, right_v)
        return dfs(root,float("-inf"), float("inf"))

slt = Solution()    
# Test Case
bst = TreeNode(8, TreeNode(5, TreeNode(2, None, TreeNode(3)),TreeNode(6)),TreeNode(10,None,TreeNode(14)))
slt.isValidBST(bst)

"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [2,1,3]
    Output: true

Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1
"""