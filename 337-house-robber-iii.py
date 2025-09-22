# https://leetcode.com/problems/house-robber-iii

from typing import Optional
from functools import cache

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dfs(node,canRob):
            if not node:
                return 0
            if not canRob:
                return dfs(node.left, True) + dfs(node.right, True)

            val1 = node.val + dfs(node.left,False) + dfs(node.right,False)
            val2 = dfs(node.left,True) + dfs(node.right,True)
            return max(val1,val2)
            
        return dfs(root,True)


