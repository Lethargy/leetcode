# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from sortedcontainers import SortedSet

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        seen = SortedSet()

        def dfs(node):
            if not node:
                return
            
            seen.add(node.val)
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        if len(seen) >= 2:
            return seen[1]
        else:
            return -1