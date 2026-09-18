class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = row
        dq = deque()
        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        farthest = [[float("inf")] * col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    dq.append((r, c, 0))
                    farthest[r][c] = 0
        while dq:
            r, c, distance = dq.popleft()
            if distance > farthest[r][c]:
                continue
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < row and 0 <= nc < col):
                    continue
                if distance + 1 < farthest[nr][nc]:
                    farthest[nr][nc] = distance + 1
                    dq.append((nr, nc, distance + 1))
        heap = []
        heapq.heappush(heap,(-farthest[0][0],0,0))
        
        visited = set()
        visited.add((0,0))
        maxx = [[float("-inf")] * col for _ in range(row)]
        maxx[0][0] = farthest[0][0]
        while heap:
            far , r, c = heapq.heappop(heap)
            if r== row-1 and c== col-1:
                return -far
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < row and 0 <= nc < col) or grid[nr][nc]==1:
                    continue
                minn = min(-far, farthest[nr][nc])
                if minn> maxx[nr][nc]:
                    maxx[nr][nc] = minn
                    heapq.heappush(heap,(-minn,nr,nc))

        return max(0, maxx[row-1][col-1])

        






        
        
        








        