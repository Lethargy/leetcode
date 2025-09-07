# https://leetcode.com/problems/evaluate-boolean-binary-tree

from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# post order DFS

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not (node.left or node.right):
                return bool(node.val)
            
            L = dfs(node.left)
            R = dfs(node.right)

            if node.val == 2:
                return L or R
            elif node.val == 3:
                return L and R
            
        return dfs(root)