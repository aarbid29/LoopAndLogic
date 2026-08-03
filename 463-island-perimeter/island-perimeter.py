class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        visited = set()
        perim = 0

        def dfs(r,c):
            nonlocal perim
            if (r,c) in visited:
                return 
            
            visited.add((r,c))

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    perim += 1
                    continue

                if grid[nr][nc] != 1:
                    perim += 1
                    continue

                dfs(nr,nc)
            

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue
                dfs(r,c)

        return perim