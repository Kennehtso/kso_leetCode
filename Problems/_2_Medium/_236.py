from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if not root: return None
            l = self.lowestCommonAncestor(root.left, p, q)
            r = self.lowestCommonAncestor(root.right, p, q)
            if (l and r ) or root == p or root == q:
                return root
            return l or r

slt = Solution() 
# Test Case
_0 = TreeNode(0, None, None)
_1 = TreeNode(1, None, None)
_2 = TreeNode(2, None, None)
_3 = TreeNode(3, None, None)
_4 = TreeNode(4, None, None)
_5 = TreeNode(5, None, None)
_6 = TreeNode(6, None, None)
_7 = TreeNode(7, None, None)
_8 = TreeNode(8, None, None)
_2.left = _7
_2.right = _4
_5.left = _6
_5.right = _2
_1.left = _0
_1.right = _8
_3.left = _5
_3.right = _1
slt.lowestCommonAncestor(_3, _4, _8)
"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: 
    “The lowest common ancestor is defined between two nodes p and q as 
    the lowest node in T that has both p and q as descendants
    (where we allow a node to be a descendant of itself).”


Example 1:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
    Input: root = [1,2], p = 1, q = 2
    Output: 1

 
Constraints:
    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the tree.

"""