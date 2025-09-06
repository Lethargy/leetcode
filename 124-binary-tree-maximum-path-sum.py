# https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        global ans
        ans = -float('inf')

        def dfs(node):
            if not node:
                return -float('inf')

            L = max(0, dfs(node.left))
            R = max(0, dfs(node.right))
            global ans
            ans = max(ans, node.val + L + R)
            return max(node.val + L, node.val + R)

        dfs(root)
        return ans