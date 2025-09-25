# https://leetcode.com/problems/cousins-in-binary-tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# dfs
        
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.xdepth = None
        self.ydepth = None
        self.xparent = None
        self.yparent = None

        def dfs(node, prev, depth):
            if not node:
                return
            
            if node.val == x:
                self.xdepth = depth
                self.xparent = prev
            
            if node.val == y:
                self.ydepth = depth
                self.yparent = prev
            
            dfs(node.left, node, depth+1)
            dfs(node.right, node, depth+1)
    
        dfs(root,None,0)

        if self.xdepth == self.ydepth and self.xparent != self.yparent:
            return True
        else:
            return False

# bfs

from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xdepth = None
        ydepth = None
        xparent = None
        yparent = None
        
        queue = deque([(root,None,0)])

        while queue:
            node, prev, depth = queue.popleft()

            if not node:
                continue
            
            if node.val == x:
                xdepth = depth
                xparent = prev
            
            if node.val == y:
                ydepth = depth
                yparent = prev
            
            queue.append((node.left,node,depth+1))
            queue.append((node.right,node,depth+1))

        if xdepth == ydepth and xparent != yparent:
            return True
        else:
            return False



