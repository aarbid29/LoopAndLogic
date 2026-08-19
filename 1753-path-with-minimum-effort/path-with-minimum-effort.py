class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        distance = [[float("inf")] * len(heights[0]) for _ in range(len(heights))]
        
        heap =[]
        heapq.heappush(heap,(0,0,0))
        row = len(heights)
        col = len(heights[0])
        visited = set()

        while heap:
            val , cell_r , cell_c = heapq.heappop(heap)
            parent = heights[cell_r][cell_c]

            if cell_r == row-1 and cell_c == col-1:
                return val

            for dr,dc in directions:
                nr,nc = cell_r + dr , cell_c+ dc

                if 0<=nr<row and 0<=nc<col:
                    curr_cell = heights[nr][nc]
                    abs_diff = abs(parent-curr_cell)
                    maxx = max(abs_diff,val)
                    if maxx < distance[nr][nc]:
                        distance[nr][nc]= maxx
                        heapq.heappush(heap,(distance[nr][nc],nr,nc))
        
                




        