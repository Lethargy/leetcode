# https://leetcode.com/problems/validate-binary-search-tree

from typing import Optional
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# in-order traversal DFS
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -inf
        self.ans = True

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            if node.val <= self.prev:
                self.ans = False
            else:
                self.prev = node.val
            dfs(node.right)

        dfs(root)
        return self.ans