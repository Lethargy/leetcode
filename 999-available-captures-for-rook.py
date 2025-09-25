# https://leetcode.com/problems/available-captures-for-rook

from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    i0 = i
                    j0 = j
                    break
        
        ans = 0

        for d in [(-1, 0), (1,0), (0,-1), (0,1)]:
            i = i0
            j = j0

            while 0 <= i < 8 and 0 <= j < 8:
                if board[i][j] == 'R' or board[i][j] == '.':
                    i += d[0]
                    j += d[1]
                elif board[i][j] == 'p':
                    ans += 1
                    break
                else:
                    break

        return ans
            