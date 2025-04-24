# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# preorder traversal DFS
def maxDepth(root):
    if root is None:
        return 0 # no tree, no depth

    ans = 0
    def dfs(node, depth):
        if not (node.left or node.right):
            nonlocal ans
            ans = max(ans, depth)
            return

        if node.left:
            dfs(node.left, depth+1)

        if node.right:
            dfs(node.right, depth+1)

    dfs(root,1)
    return ans

# BFS
def maxDepth(root):
    if root is None:
        return 0 # no tree, no depth

    count = 1 # if there is an initial node, we start at 1
    q = [root] # initilize q
    while q:
        p = [] # queue for next layer
        for node in q:
            if node.left: # add existing children onto next layer
                p.append(node.left)
            if node.right:
                p.append(node.right)
        if p: # if there is a next layer, add 1 to count
            count = count + 1
            
        q = p

    return count