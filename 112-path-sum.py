# https://leetcode.com/problems/path-sum

from collections import deque
from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
# DFS

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:           
        def dfs(node,target):
            if not node:
                return False
            if not (node.left or node.right): # leaf
                return target == node.val
            return dfs(node.left, target-node.val) or dfs(node.right, target-node.val)

        return dfs(root,targetSum)
    
# BFS

from collections import deque

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:           
        
        queue = deque([(root,targetSum)])
        while queue:
            node, target = queue.popleft()
            if not node:
                continue
            if not (node.left or node.right):
                if target == node.val:
                    return True
                else:
                    continue
            queue.append((node.left, target-node.val))
            queue.append((node.right, target-node.val))

        return False