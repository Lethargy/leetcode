# https://leetcode.com/problems/symmetric-tree/

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
    
        val = items.popleft()
        if val is not None:
            node.right = TreeNode(val)
            queue.append(node.right)

    return root

# BFS
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not (root.left or root.right):
            return True

        queue = deque([(root.left,root.right)])
        while queue:
            L, R = queue.popleft()
            if not L or not R:
                if L != R:
                    return False
                else:
                    continue
            if L.val != R.val:
                return False
            queue.append((L.left,R.right))
            queue.append((L.right,R.left))
        
        return True


# DFS
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(L,R):
            if not L or not R:
                return L == R
            if L.val != R.val:
                return False
            return dfs(L.left, R.right) and dfs(L.right, R.left)

        return dfs(root.left,root.right)