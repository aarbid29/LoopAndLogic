class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        heap = []

        def dfs(r, c):
            if not (0 <= r < row and 0 <= c < col):
                return
            if (r, c) in visited or grid[r][c] == 0:
                return
            visited.add((r, c))
            grid[r][c] = "#"
            heapq.heappush(heap, (0, r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        found = False

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
            if found:
                break

        while heap:
            flips, r, c = heapq.heappop(heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < row and 0 <= nc < col):
                    continue

                if grid[nr][nc] == 1:
                    return flips

                if grid[nr][nc] == 0:
                    grid[nr][nc] = "#"
                    heapq.heappush(heap, (flips + 1, nr, nc))