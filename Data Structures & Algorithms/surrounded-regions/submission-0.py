class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])

        def dfs(r,c):
            if not (0 <= r < row and 0 <= c < col) or board[r][c] != 'O':
                return 
            
            board[r][c] = 'T'
            for dr, dc in ((0,1), (1,0), (0,-1), (-1,0)):
                dfs(r + dr, c + dc)

        for r in range(row):
            dfs(r, 0)
            dfs(r, col - 1)

        for c in range(col):
            dfs(0, c)
            dfs(row - 1, c)

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'