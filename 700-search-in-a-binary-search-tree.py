# https://leetcode.com/problems/search-in-a-binary-search-tree

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# DFS
        
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            if node.val == val:
                return node
            if node.val > val:
                return dfs(node.left)
            if node.val < val:
                return dfs(node.right)

        return dfs(root)
    
# BFS

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                continue
            if node.val == val:
                return node
            if node.val > val:
                queue.append(node.left)
            if node.val < val:
                queue.append(node.right)

        return None