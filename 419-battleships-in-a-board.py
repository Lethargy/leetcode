# https://leetcode.com/problems/battleships-in-a-board/description

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        n = len(board)
        k = len(board[0])
        ans = 0

        def dfs(i,j):
            stack = [(i,j)]

            while stack:
                r0,c0 = stack.pop()
                board[r0][c0] = '.'

                for r1,c1 in [(r0+1,c0), (r0-1,c0), (r0,c0-1), (r0,c0+1)]:
                    if not (0 <= r1 < n and 0 <= c1 < k):
                        continue

                    if board[r1][c1] == 'X':
                        stack.append((r1,c1))
        
        for i in range(n):
            for j in range(k):
                if board[i][j] == 'X':
                    dfs(i,j)
                    ans = ans + 1

        return ans