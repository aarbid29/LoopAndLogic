class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        maxx = 0 

        def dfs(r,c):
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))
            area = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                if grid[nr][nc] == 1:
                    area += dfs(nr,nc)

            return area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue
                
                vall = dfs(r,c)
                maxx = max(maxx, vall)

        return maxx