from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:      
        def check(_left, _right):
            if not _left and not _right: 
                return True
            if  _left and not _right or not _left and _right: 
                return False
            # Only switch left side
            _left.left, _left.right = _left.right, _left.left
            return check(_left.left, _right.left) and check(_left.right, _right.right) and _left.val == _right.val
        return check(root.left, root.right)
        """
                     1
            2               3
        4       5       6       7


                     1
            2               3
        5       4       6       7
        """
            
slt = Solution()
#True
_7 = TreeNode(3,None,None)
_6 = TreeNode(4,None,None)
_5 = TreeNode(4,None,None)
_4 = TreeNode(3,None,None)
_3 = TreeNode(2,_6,_7)
_2 = TreeNode(2,_4,_5)
_root = TreeNode(1,_2,_3)
slt.isSymmetric(_root)
"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Example 1:
    Input: root = [1,2,2,3,4,4,3]
    Output: true

Example 2:
    Input: root = [1,2,2,null,3,null,3]
    Output: false

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
"""