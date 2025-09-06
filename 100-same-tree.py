# https://leetcode.com/problems/same-tree/description/

from collections import deque
from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_binary_tree(items):
    if not items:
        return None

    items = deque(items)
    root = TreeNode(items.popleft())
    queue = deque([root])
    
    while items:
        node = queue.popleft()
        val = items.popleft()
        if val is not None:
            node.left = TreeNode(val)
            queue.append(node.left)
    
        val = items.popleft() if items else None
        if val is not None:
            node.right = TreeNode(val)
            queue.append(node.right)

    return root

# DFS

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):           
            if not p or not q:
                return p == q
            if p.val != q.val:
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p,q)
        

# BFS

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p,q)])

        while queue:
            p,q = queue.popleft()
            if not p or not q:
                if p != q:
                    return False
                else:
                    continue
            if p.val != q.val:
                return False
            queue.append((p.left, q.left))
            queue.append((p.right, q.right))

        return True