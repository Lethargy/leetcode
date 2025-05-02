# https://leetcode.com/problems/path-sum-ii/description

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
# DFS iterative

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ans = []
        stack = [(root, [root.val])]

        while stack:
            node, runningPath = stack.pop()

            if not (node.left or node.right) and sum(runningPath) == targetSum:
                ans.append(runningPath)

            if node.left:
                stack.append((node.left, runningPath + [node.left.val]))

            if node.right:
                stack.append((node.right, runningPath + [node.right.val]))

        return ans