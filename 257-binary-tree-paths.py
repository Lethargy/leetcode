# https://leetcode.com/problems/binary-tree-paths

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# DFS
        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def dfs(node,path):
            path = path + str(node.val)

            if not (node.left or node.right):
                ans.append(path)
                return

            if node.left:
                dfs(node.left, path + '->')

            if node.right:
                dfs(node.right, path + '->')

        dfs(root,'')

        return ans