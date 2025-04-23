# https://leetcode.com/problems/path-sum

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS iterative

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, runningSum = stack.pop()

            if not (node.left or node.right) and runningSum == targetSum:
                return True

            if node.left:
                stack.append((node.left, runningSum + node.left.val))

            if node.right:
                stack.append((node.right, runningSum + node.right.val))

        return False