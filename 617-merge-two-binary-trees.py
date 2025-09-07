# https://leetcode.com/problems/merge-two-binary-trees

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional
        
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if not node1 and not node2:
                return None

            out = TreeNode()
            if node1 and node2:
                out.val = node1.val + node2.val
                out.left = dfs(node1.left, node2.left)
                out.right = dfs(node1.right, node2.right)
            if node1 and not node2:
                out.val = node1.val
                out.left = dfs(node1.left, None)
                out.right = dfs(node1.right, None)
            if node2 and not node1:
                out.val = node2.val
                out.left = dfs(None, node2.left)
                out.right = dfs(None, node2.right)
            
            return out

        return dfs(root1,root2)
        