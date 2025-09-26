# https://leetcode.com/problems/diameter-of-binary-tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0

            L = dfs(node.left) # deepest from left downward
            R = dfs(node.right) # deepest from right downward

            self.ans = max(self.ans, L+R)

            return 1 + max(L,R)
        
        dfs(root)
        return self.ans
            