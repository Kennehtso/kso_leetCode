from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        r = []
        def bfs(root: TreeNode, level:int):
            if not root: return
            if level > len(r):
                r.append([root.val])  
            else:
                if level % 2 == 0:
                    r[level-1].insert(0, root.val)
                else:
                    r[level-1].append(root.val)
            bfs(root.left, level + 1)   
            bfs(root.right, level + 1)
        bfs(root, 1)
        return r

slt = Solution() 
# Test Case
root = TreeNode(8, TreeNode(5, TreeNode(2, None, TreeNode(3)),TreeNode(6)),TreeNode(10,None,TreeNode(14)))
slt.zigzagLevelOrder(root)
"""
103. Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
 (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

"""