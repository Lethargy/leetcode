# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# preorder traversal DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))

        return dfs(root)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node):
            if not (node.left or node.right):
                return 1
            if node.left and not node.right:
                return 1 + dfs(node.left)
            if node.right and not node.left:
                return 1 + dfs(node.right)
            return 1 + max(dfs(node.left), dfs(node.right))

        return dfs(root)

# BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        queue = deque([root])
        while queue:
            ans = ans + 1
            new_queue = deque([])
            while queue:
                node = queue.popleft()
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return ans