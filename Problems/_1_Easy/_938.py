from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def doWork(node,low,high):
            if low <= node.val <= high:
                self.total += node.val
            if node.left is not None :
                doWork(node.left,low,high)
            if node.right is not None:
                doWork(node.right,low,high)
                
        self.total = 0
        doWork(root, low, high)
        print(self.total)
        return self.total
      
        
slt = Solution()
_8 = TreeNode(8,None,None)
_7 = TreeNode(7,None,_8)
_6 = TreeNode(6,None,None)
_4 = TreeNode(4,_6,_7)
_5 = TreeNode(5,None,None)
_3 = TreeNode(3,None,None)
_2 = TreeNode(2,_4,_5)
_root = TreeNode(1,_2,_3)

slt.rangeSumBST(_root,1,8)


"""
938. Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

 

Example 1:
    Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    Output: 32

Example 2:
    Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    Output: 23
 

Constraints:
    The number of nodes in the tree is in the range [1, 2 * 104].
    1 <= Node.val <= 105
    1 <= low <= high <= 105
    All Node.val are unique.

"""