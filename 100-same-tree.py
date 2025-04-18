# https://leetcode.com/problems/same-tree/description/

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
    
        val = items.popleft() if items else None
        if val is not None:
            node.right = TreeNode(val)
            queue.append(node.right)

    return root

# DFS iterative

def isSameTree(p,q):
    # create two stacks, both initialized with start nodes
    P = [p]
    Q = [q]

    while P or Q:
        # while at least one stack is not empty, pull first item from each
        x = P.pop()
        y = Q.pop()

        if not x or not y: # if one is a NoneType...
            if x != y: # check whether both are
                return False
            else:
                continue

        if x.val != y.val: # if neither are None, check values
            return False

        # once the above clears, append children to stack
        P.append(x.right)
        P.append(x.left)
        Q.append(y.right)
        Q.append(y.left)

    return True

# DFS recursive, without helper function

def isSameTree(p,q):
    # if one is a NoneType, check if both are
    if not p or not q:
        return p == q

    # if both exist, compare values
    if p.val != q.val:
        return False

    # pre-order traversal
    L = isSameTree(p.left, q.left)
    R = isSameTree(p.right, q.right)

    # if everything looks good, recursive call
    return L and R

# DFS recursive, with helper function

def isSameTree(p,q):
    ans = True

    def dfs(p,q):
        nonlocal ans
        
        if not p or not q:
            ans = p == q
            return

        if p.val != q.val:
            ans = False
            return
            
        # pre-order traversal
        dfs(p.left, q.left)
        dfs(p.right, q.right)

    dfs(p,q)
    return ans

# BFS
def isSameTree(p,q):
    # create two queues, both initialized with start nodes
    P = [p]
    Q = [q]

    while P or Q:
    # while at least one queue is not empty, pull first item from each
        x = P.pop(0)
        y = Q.pop(0)

        # first, make sure these items are not NoneTypes
        if x and y:
            # then, compare their values
            if x.val == y.val:
                # if they match, add their children to respective queues
                P.append(x.left)
                P.append(x.right)
                Q.append(y.left)
                Q.append(y.right)
            else:
                # otherwise, trees are not the same
                return False

        # if both are NoneTypes, we have reached the end of a tree
        elif not x and not y:
            continue

        # if one is a NoneType and the other is not, trees are not the same
        else:
            return False

    return True