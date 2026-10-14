class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = {(0, 0)}
        heap= [(0, 0, 0)]
        cost = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        costpercell =[[float("inf")]*col for  _ in range(row)]
        costpercell[0][0] = 0

        while heap :
            cost , r ,c = heapq.heappop(heap)
            if r == row - 1 and c == col - 1:
                return cost
            if cost > costpercell[r][c]:
                continue
            val = grid[r][c]

            if val == 1:
                vr, vc = r, c + 1
            elif val == 2:
                vr, vc = r, c - 1
            elif val == 3:
                vr, vc = r + 1, c
            else:
                vr, vc = r - 1, c
            

            for dr,dc in directions:
                nr ,nc = dr+r , dc+c 

                if not(0<= nr <row and 0<= nc < col):
                    continue
                
                
                if nr == vr and nc == vc:

                    if costpercell[nr][nc] > cost:
                        costpercell[nr][nc]=cost
                        heapq.heappush(heap,(cost , nr , nc))
                else:

                    if costpercell[nr][nc] > cost+1:
                        costpercell[nr][nc]=cost+1
                        heapq.heappush(heap,(cost +1, nr , nc))




