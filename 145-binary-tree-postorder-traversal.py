# https://leetcode.com/problems/binary-tree-postorder-traversal/description

def postorderTraversal(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    if not root:
        return []
        
    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)

        if node.right:
            stack1.append(node.right)

    return [node.val for node in stack2[::-1]]
    
    
def postorderTraversal(root):
    if not root:
        return []

    L = postorderTraversal(root.left)
    R = postorderTraversal(root.right)
    
    return L + R + [root.val]