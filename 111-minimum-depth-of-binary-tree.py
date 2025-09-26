# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from math import inf

# DFS

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        self.ans = inf

        def dfs(node,depth):
            if not (node.left or node.right):
                self.ans = min(self.ans,depth)
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
        
        dfs(root,1)
        return self.ans

# BFS

from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        ans = 0
        while queue:
            nextQueue = deque([])
            ans = ans + 1
            while queue:
                node = queue.popleft()
                if not (node.left or node.right):
                    return ans
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            queue = nextQueue