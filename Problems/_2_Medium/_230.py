from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cnt, ans = k, -1
        def dfs_in_order(bst: TreeNode):
            nonlocal cnt
            nonlocal ans
            if not bst or ans != -1: return
            dfs_in_order(bst.left) 
            cnt -= 1
            if cnt == 0:
                ans = bst.val
            dfs_in_order(bst.right)
            return
        dfs_in_order(root)
        print(ans)
        return ans

slt = Solution() 
# Test Case
bst = TreeNode(8, TreeNode(5, TreeNode(2, None, TreeNode(3)),TreeNode(6)),TreeNode(10,None,TreeNode(14)))
slt.kthSmallest(bst, 4)
"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
    Input: root = [3,1,4,null,2], k = 1
    Output: 1

Example 2:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3
 

Constraints:
    The number of nodes in the tree is n.
    1 <= k <= n <= 104
    0 <= Node.val <= 104

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

"""