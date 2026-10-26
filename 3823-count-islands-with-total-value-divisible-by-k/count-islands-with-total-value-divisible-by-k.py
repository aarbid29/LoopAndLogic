class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        row = len(grid)
        col = len(grid[0])

        directions= [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        def dfs(r,c):
            visited.add((r,c))
            res = 0
            for dr,dc in directions:
                nr , nc = dr+r , dc+c
                if not(0<=nr < row and 0<= nc <col) or (nr,nc) in visited:
                    continue
                
                if grid[nr][nc]!=0:
                    res += dfs(nr,nc)
            return res+ grid[r][c]
            

        island = 0 
        for r in range(row):
            for c in range(col):
                if grid[r][c]!=0 and (r,c)not in visited:
                    ans = dfs(r,c)
                    if ans % k ==0:
                        island+=1
        return island
        