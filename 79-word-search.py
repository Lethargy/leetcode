# https://leetcode.com/problems/word-search/description/

# backtracking

def exist(board, word):
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

# tests
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word)) # True

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(exist(board, word)) # True

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(exist(board, word)) # False