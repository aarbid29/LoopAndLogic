class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        row= len(grid)
        col = len(grid[0])
        visited =set()
        boundary = False

        def dfs(r,c):
            nonlocal boundary
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = dr+r , dc+c
                if not (0<=nr <row and 0<=nc < col)or (nr,nc)in visited:
                    continue
                if grid[nr][nc]==0:
                    #land cannot touch the boundary
                    if (nr==0 or nr == row-1) or (nc ==0 or nc==col-1):
                        boundary =True
                    dfs(nr,nc)
  

        island = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==0 and (r,c)not in visited and not((r==0 or r == row-1) or (c ==0 or c==col-1)) :
                    boundary = False
                    dfs(r,c)
                    if not boundary:
                        island+=1
                    
        return island



        