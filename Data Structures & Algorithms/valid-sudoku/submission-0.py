class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i : set() for i in range(9)}
        cols = {i : set() for i in range(9)}
        blocks = {(x, y) : set() for x in range(3) for y in range(3)}
        
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                
                else:
                    if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in blocks[(r // 3, c // 3)]:
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    blocks[(r // 3, c // 3)].add(board[r][c])
        
        return True