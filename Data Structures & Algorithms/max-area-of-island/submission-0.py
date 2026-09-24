class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        N, M = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= N or j < 0 or j >= M or grid[i][j] != 1:
                return 0

            area = 1
            grid[i][j] = 0
            for dr, dc in dirs:
                area += dfs(i + dr, j + dc)
            return area
            
        
        res = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 1:
                    res = max(res, dfs(r, c))
        return res