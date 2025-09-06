# https://leetcode.com/problems/maximum-width-of-binary-tree

from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = deque([(root,0)])
        ans = -float('inf')

        while queue:
            ans = max(ans, 1 + queue[-1][1] - queue[0][1])

            new_queue = deque([])
            while queue:
                node, k = queue.popleft()

                if node.left:
                    new_queue.append((node.left, 2*k))

                if node.right:
                    new_queue.append((node.right, 2*k+1))

            queue = new_queue

        return ans