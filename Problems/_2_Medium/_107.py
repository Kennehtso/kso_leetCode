from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result, dq = [], deque([root])
        while dq:
            lv_list = []
            for _ in range(len(dq)):
                node = dq.popleft()
                lv_list.append(node.val)
                for node in [node.left, node.right]:
                    if node: dq.append(node) 
            result.append(lv_list)
        result.reverse()
        return result

slt = Solution() 
# Test Case
root = TreeNode(8, TreeNode(5, TreeNode(2, None, TreeNode(3)),TreeNode(6)),TreeNode(10,None,TreeNode(14)))
slt.levelOrderBottom(root)
"""
107. Binary Tree Level Order Traversal II

Given the root of a binary tree, 
return the bottom-up level order traversal of its nodes' values. 
(i.e., from left to right, level by level from leaf to root).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[15,7],[9,20],[3]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""