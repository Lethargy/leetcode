# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [None]
        count = [0]

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            
            count[0] += 1
            if count[0] == k:
                ans[0] = node.val
                return

            dfs(node.right)

        dfs(root)
        return ans[0]