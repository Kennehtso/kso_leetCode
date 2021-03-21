from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right

class Solution:
    ans = True
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.compareVal(p, q)
        print(True)
        return self.ans
    
    def compareVal(self, p: TreeNode, q: TreeNode):
        if self.ans is True:
            val_p = p.val if p is not None else None
            val_q = q.val if q is not None else None
            """
            print(f"-----compare--------")
            print(f"p: {val_p}")
            print(f"q: {val_q}")
            print(f"-------------------")
            """
            
            if val_p != val_q:
                print(f"val_p != val_q: {val_p} != {val_q}")
                self.ans = False
            elif p or q:
                p_l = p.left if p and p.left else None
                p_r = p.right if p and p.right else None
                q_l = q.left if q and q.left else None
                q_r = q.right if q and q.right else None
                self.compareVal(p_l, q_l)
                self.compareVal(p_r, q_r)

slt = Solution()    
_5 = TreeNode(3,None,None)
_4 = TreeNode(2,None,None)
_p = TreeNode(1,_4,_5)
_3 = TreeNode(3,None,None)
_2 = TreeNode(2,None,None)
_q = TreeNode(1,_2,_3)
# Test Case
slt.isSameTree(_p,_q)
"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
 

Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false

Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false

Constraints:
    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104

"""
