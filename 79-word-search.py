# https://leetcode.com/problems/word-search/description/

# backtracking / DFS

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(board)
        K = len(board[0])
        L = len(word)
        
        start = []
        
        for i in range(N):
            for j in range(K):
                if board[i][j] == word[0]:
                    start.append((i,j))

        for i0,j0 in start:
            stack = [(i0,j0,{(i0,j0)})]
            
            while stack:
                i,j,p = stack.pop()
            
                if len(p) == L:
                    return True
            
                for r,c in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if not (0 <= r <= N-1) or not (0 <= c <= K-1):
                        continue

                    if (r,c) in p:
                        continue
                        
                    if board[r][c] == word[len(p)]:
                        stack.append((r,c,p|{(r,c)}))
                        
        return False

# recursive DFS

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        L = len(word)
        m = len(board)
        n = len(board[0])

        global ans
        ans = False

        def dfs(i,j,k):
            global ans
            if board[i][j] != word[k]:
                return

            if k == L-1:
                ans = True
                return
            
            t = board[i][j]
            board[i][j] = '*'
            
            for r,c in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if not (0 <= r < m and 0 <= c < n):
                    continue
                dfs(r,c,k+1)
            
            board[i][j] = t

        for i in range(m):
            for j in range(n):
                dfs(i,j,0)

        return ans