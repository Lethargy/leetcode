# https://leetcode.com/problems/path-sum-ii/description

from typing import Optional, List
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# BFS

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []

        ans = []
        queue = deque([(root, [root.val])])

        while queue:
            node, runningPath = queue.popleft()

            if not (node.left or node.right) and sum(runningPath) == targetSum:
                ans.append(runningPath)

            if node.left:
                queue.append((node.left, runningPath + [node.left.val]))

            if node.right:
                queue.append((node.right, runningPath + [node.right.val]))

        return ans
    
    
# DFS, no global accumulator
    
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(node, targetSum, path):
            if not node:
                return None
        
            if not (node.left or node.right):
                if node.val == targetSum:
                    ans.append(path + [node.val])
        
            dfs(node.left, targetSum - node.val, path + [node.val])
            dfs(node.right, targetSum - node.val, path + [node.val])

        dfs(root, targetSum, [])
        return ans

# DFS, no global accumulator

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, targetSum, path = []):
            if not node:
                return []
        
            if not (node.left or node.right):
                if node.val == targetSum:
                    return [path + [node.val]]
        
            return (dfs(node.left, targetSum - node.val, path + [node.val]) + 
            dfs(node.right, targetSum - node.val, path + [node.val]))

        return dfs(root, targetSum)