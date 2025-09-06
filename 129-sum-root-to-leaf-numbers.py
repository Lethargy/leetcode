# https://leetcode.com/problems/sum-root-to-leaf-numbers

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        out = {'ans':0}

        def backtrack(node, s):
            new_s = 10 * s + node.val
            
            if not (node.left or node.right):
                out['ans'] = out['ans'] + new_s
                return

            if node.left:
                backtrack(node.left, new_s)

            if node.right:
                backtrack(node.right, new_s)

        backtrack(root, 0)
        return out['ans']
    
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node,S,T):
            S = 10 * S + node.val
            
            if not (node.left or node.right):
                T = T + S 

            if node.left:
                T = dfs(node.left, S, T)
            
            if node.right:
                T = dfs(node.right, S, T)

            return T

        return dfs(root,0,0)