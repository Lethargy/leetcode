# https://leetcode.com/problems/subtree-of-another-tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p,q):
            if not p or not q:
                return p == q

            if p.val != q.val:
                return False
            
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

        def dfs(node):
            if not node:
                return False

            if node.val == subRoot.val:
                if isSameTree(node,subRoot):
                    return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)