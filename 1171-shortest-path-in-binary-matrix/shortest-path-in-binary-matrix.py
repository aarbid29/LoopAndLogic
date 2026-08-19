class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col= len(grid[0])
        if grid[0][0]!=0:
            return -1
        if grid[row-1][col-1]!=0:
            return -1
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1),(-1,1),(1,1),(-1,-1)]
        dq = deque()
        dq.append((0,0))
        heap = []
        lvl = 0
        visited = set()
        visited.add((0,0))

        while dq:
            lvl+=1
            size = len(dq)

            for i in range(len(dq)):
                cell_r , cell_c = dq.popleft()

                if cell_r==row-1 and cell_c==col-1:
                    return lvl

                for dr,dc in directions:
                    nr= cell_r + dr
                    nc = cell_c + dc
                    if (nr,nc)in visited:
                        continue
                    if 0<=nr<row and 0<=nc<col:
                    
                        if grid[nr][nc]==0:
                            visited.add((nr,nc))
                            dq.append((nr,nc))
        return -1


        





        


        