# https://leetcode.com/problems/two-sum-iv-input-is-a-bst

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(node):
            if not node:
                return False
            
            L = dfs(node.left)

            if k - node.val in seen:
                return True
            
            seen.add(node.val)

            R = dfs(node.right)

            return L or R

        return dfs(root)