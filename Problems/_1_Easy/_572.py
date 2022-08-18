# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def dfs(root, sub):
            if not root: return
            isFound = False
            if sub and sub.val == root.val:
                isFound = check(root, sub)
            isFound = isFound or dfs(root.left, sub) or dfs(root.right, sub)
            return isFound
              
        def check(root, sub):
            if not root and not sub: return True
            if (not root and sub) or (root and not sub): return False
            l_same = check(root.left, sub.left)
            r_same = check(root.right, sub.right)
            return l_same and r_same and root.val == sub.val
        
        res = dfs(root, subRoot)
        #print(res)
        return res
    """
    r = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def gogo(root: TreeNode, locateMsg):
            #print(locateMsg+" **************")
            if root is None:
                return 0
            left = gogo(root.left, f"Going Left of {root.val}")
            #print(f"left: {left}")
            right = gogo(root.right,  f"Going Right of {root.val}")
            #print(f"right: {right}")
            self.r = max(self.r,left+right+1)
            #print(f"max - self.r: {self.r}")
            return max(left, right) + 1

        gogo(root,"ROOT")
        #print(f"self.r: {self.r-1}")
        return self.r - 1 if self.r > 0 else 0
    """
slt = Solution()
# Test Case
#result = slt.longestCommonPrefix(["dog","racecar","car"])
_8 = TreeNode(8,None,None)
_7 = TreeNode(7,None,_8)
_6 = TreeNode(6,None,None)
_4 = TreeNode(4,_6,_7)
_5 = TreeNode(5,None,None)
_3 = TreeNode(3,None,None)
_2 = TreeNode(2,_4,_5)
_root = TreeNode(1,_2,_3)

slt.diameterOfBinaryTree(_root)

"""
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

Example 2:
    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false

Constraints:
    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].
    -104 <= root.val <= 104
    -104 <= subRoot.val <= 104

"""