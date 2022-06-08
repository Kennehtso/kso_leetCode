from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val         
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: TreeNode) -> TreeNode:
        if not root: return
        dq, dq2 = deque([root]), deque()
        while dq:
            cur = dq.popleft()
            if cur.left: dq2 += [cur.left]
            if cur.right:  dq2 += [cur.right]
            if not dq:
                dq = dq2
                dq2 = deque()
            elif cur:
                cur.next = dq[0]
        return root

slt = Solution()    
# Test Case
root = TreeNode(8, TreeNode(5, TreeNode(2, None, TreeNode(3)),TreeNode(6)),TreeNode(10,None,TreeNode(14)))
slt.connect(root)

"""
117. Populating Next Right Pointers in Each Node II

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

 
Example 1:
    Input: root = [1,2,3,4,5,null,7]
    Output: [1,#,2,3,#,4,5,7,#]
    Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:
    Input: root = []
    Output: []


Constraints:
    The number of nodes in the tree is in the range [0, 6000].
    -100 <= Node.val <= 100


Follow-up:

    You may only use constant extra space.
    The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

"""