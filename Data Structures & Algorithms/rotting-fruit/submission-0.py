class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        row, col = len(grid), len(grid[0])
        fresh = 0
        time = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c,0))

        while fresh and q:
            r,c,time = q.popleft()
            for dr, dc in ((0,1), (1,0), (0,-1), (-1,0)):
                nr,nc = r+dr, c+dc
                if (0 <= nr < row and 0 <= nc < col) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr,nc,time + 1))

        return -1 if fresh else (q[-1][2] if q else time)