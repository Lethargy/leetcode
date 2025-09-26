# https://leetcode.com/problems/average-of-levels-in-binary-tree

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# dfs
        
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = deque([root])

        while queue:
            nodeSum = 0
            nodeCount = 0
            newQueue = deque([])
            while queue:
                node = queue.popleft()
                nodeSum += node.val
                nodeCount += 1
                if node.left: newQueue.append(node.left)
                if node.right: newQueue.append(node.right)
            ans.append(nodeSum/nodeCount)
            queue = newQueue
            
        return ans