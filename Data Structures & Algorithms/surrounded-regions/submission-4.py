class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfsReplace(r,c):
            if 0 > c or 0 > r or r >= m or c >= n or board[r][c] != "O":
                return
            
            board[r][c] = "."
            dfsReplace(r-1,c)
            dfsReplace(r+1,c)
            dfsReplace(r,c+1)
            dfsReplace(r,c-1)

        for r in range(m):
            if board[r][0] == "O":
                dfsReplace(r, 0)
            if board[r][n - 1] == "O":
                dfsReplace(r, n - 1)

        for c in range(n):
            if board[0][c] == "O":
                dfsReplace(0, c)
            if board[m - 1][c] == "O":
                dfsReplace(m - 1, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                
                if board[r][c] == ".":
                    board[r][c] = "O"
        