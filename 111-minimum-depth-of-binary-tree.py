# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# DFS iterative

def minDepth(root):
    if root == None:
        return 0

    stack = [root]
    count = [1]
    m = float('inf') # running minimum
    while stack:
        node = stack.pop()
        c = count.pop()

        if c >= m: # already worse than current best leaf
            continue

        if not node.left and not node.right: # better leaf
            m = min(m,c)

        if node.right:
            stack.append(node.right)
            count.append(c + 1)

        if node.left:
            stack.append(node.left)
            count.append(c + 1)

    return m

# DFS recursive

def minDepth(root):
    if not root:
        return 0

    ans = float('inf')
    
    def dfs(node, depth):
        if not (node.left or node.right):
            nonlocal ans
            ans = min(ans, depth)
            return

        if node.left:
            dfs(node.left, depth + 1)

        if node.right:
            dfs(node.right, depth + 1)

    dfs(root, 1)
    return ans

# BFS

def minDepth(root):
    if root == None:
        return 0

    count = 1
    q = [root]
    while q:
        p = []
        for node in q:
            if not node.left and not node.right: # first leaf
                return count # return and stop
                
            if node.left:
                p.append(node.left)
                
            if node.right:
                p.append(node.right)

        count = count + 1
        q = p.copy()