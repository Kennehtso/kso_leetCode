from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right

class Solution:
    ans = True
    def isSymmetric(self, root: TreeNode) -> bool:
        self.compareVal(root.left, root.right)
        print(self.ans)
        return self.ans
    
    def compareVal(self, left: TreeNode, right: TreeNode):
        if self.ans is True:
            val_l = left.val if left is not None else None
            val_r = right.val if right is not None else None
            
            print(f"-----compare--------")
            print(f"left: {val_l}")
            print(f"right: {val_r}")
            print(f"-------------------")
            
            if val_l != val_r:
                self.ans = False
            elif left or right:
                l_l = left.left if left and left.left else None
                l_r = left.right if left and left.right else None
                r_l = right.left if right and right.left else None
                r_r = right.right if right and right.right else None
                self.compareVal(l_l, r_r)
                self.compareVal(r_l, l_r)
            
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