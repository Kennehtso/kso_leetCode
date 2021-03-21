from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right
        
class Solution:
    isFound = False
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool: 
        def checkValue(root, previousTotal, targetSum):
            if self.isFound or not root: 
                return
            previousTotal += root.val
            if not root.left and not root.right and  previousTotal == targetSum:
                    #print(f"!!found!!")
                    self.isFound = True
                    return 
                    
            #print(f"root.val :{root.val}")
            #print(f"previousTotal :{previousTotal}")      
            #print(f"-------------")
            checkValue(root.left, previousTotal, targetSum)
            if not self.isFound: checkValue(root.right, previousTotal, targetSum)
        if root:
            previousTotal = 0
            checkValue(root, previousTotal , targetSum)
        return self.isFound
            
slt = Solution()
_7 = TreeNode(7,None,None)
_2 = TreeNode(2,None,None)
_1 = TreeNode(1,None,None)
_11 = TreeNode(11,_7,_2)
_13 = TreeNode(13,None,None)
_4_2 = TreeNode(4,None,_1)
_4_1 = TreeNode(4,_11,None)
_8 = TreeNode(8,_13,_4_2)
_root = TreeNode(5,_4_1,_8)

slt.hasPathSum(_root, 22)
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