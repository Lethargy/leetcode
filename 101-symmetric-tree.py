# https://leetcode.com/problems/symmetric-tree/

from collections import deque

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

# DFS iterative
def isSymmetric(root):
    if not (root.left or root.right):
        return True

    stack = [(root.left,root.right)]

    while stack:
        L, R = stack.pop()

        if (L and R):
            if L.val != R.val:
                return False
            else:
                stack.append((L.left, R.right))
                stack.append((L.right, R.left))

        if not (L and R) and L != R:
            return False
    
    return True

# DFS preorder traversal
def isSymmetric(root):
    ans = True

    def dfs(L,R):
        nonlocal ans
        
        if not L or not R:
            ans = L == R
            return

        if L.val != R.val:
            ans = False
            return
        
        dfs(L.left, R.right)
        dfs(L.right, R.left)

    dfs(root.left, root.right)
    return ans