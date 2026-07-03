class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        lvl = 0
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for x, y in directions:
                    nr, nc = r + x, c + y
                    if nr > -1 and nc > -1 and nr < len(grid) and nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            lvl += 1
        return lvl if fresh == 0 else -1

