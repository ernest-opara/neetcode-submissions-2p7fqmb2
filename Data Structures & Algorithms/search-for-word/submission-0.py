class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True

            if not (0 <= r < row and 0 <= c < col) or (r,c) in path or board[r][c] != word[i]:
                return False

            path.add((r,c))
            res = max(dfs(r+1,c,i+1), dfs(r-1,c,i+1), dfs(r, c+1,i+1), dfs(r,c-1,i+1))
            path.remove((r,c))

            return res

        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False