class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        seen = set()

        def dfs(r,c,seen):
            if (r,c) in seen:
                return
            
            seen.add((r,c))
            for dr, dc in ((0,1), (1,0), (0,-1), (-1,0)):
                nr,nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, seen)

        pacific, atlantic = set(), set()
        for r in range(row):
            dfs(r,0,pacific)
            dfs(r, col-1, atlantic)
        for c in range(col):
            dfs(0, c, pacific)
            dfs(row - 1, c, atlantic)

        return [list(cell) for cell in pacific & atlantic]