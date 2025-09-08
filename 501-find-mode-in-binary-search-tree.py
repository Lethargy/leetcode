# https://leetcode.com/problems/find-mode-in-binary-search-tree/

from typing import List, Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        prev = [None]
        maxCount = [0]
        currCount = [0]

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            if node.val == prev[0]:
                currCount[0] += 1
            else:
                currCount[0] = 1
                prev[0] = node.val

            if currCount[0] > maxCount[0]:
                maxCount[0] = currCount[0]
                res[:] = [node.val]
            elif currCount[0] == maxCount[0]:
                res.append(node.val)

            dfs(node.right)

        dfs(root)
        return res
        