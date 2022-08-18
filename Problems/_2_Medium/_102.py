from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        if not root: return []
        dq, res = deque([(root, 1)]), []
        while dq:
            r, lv = dq.popleft()
            if not r: continue
            res.append([r.val]) if lv > len(res) else res[lv-1].append(r.val)
            dq.append((r.left, lv+1))
            dq.append((r.right, lv+1))
        return res

slt = Solution() 
# Test Case
root = TreeNode(8, TreeNode(5, TreeNode(2, None, TreeNode(3)),TreeNode(6)),TreeNode(10,None,TreeNode(14)))
slt.levelOrder(root)
"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

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