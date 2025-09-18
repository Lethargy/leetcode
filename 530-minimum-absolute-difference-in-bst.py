# https://leetcode.com/problems/minimum-absolute-difference-in-bst

from typing import Optional
from math import inf

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = [-inf]
        ans = [inf]

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            ans[0] = min(ans[0], node.val - prev[0])
            prev[0] = node.val
            dfs(node.right)
        
        dfs(root)
        return ans[0]