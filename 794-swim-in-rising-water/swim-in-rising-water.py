class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))

        directions = [(0,-1), (0,1), (1,0), (-1,0)]

        time = [[float("inf")] * col for _ in range(row)]
        time[0][0] = grid[0][0]

        visited = set()

        while heap:
            curr_time, cell_r, cell_c = heapq.heappop(heap)

            if (cell_r, cell_c) in visited:
                continue

            visited.add((cell_r, cell_c))

            if cell_r == row - 1 and cell_c == col - 1:
                return curr_time

            parent = grid[cell_r][cell_c]

            for dr, dc in directions:
                nr, nc = dr + cell_r, dc + cell_c

                if 0 <= nr < row and 0 <= nc < col:

                    if (nr, nc) in visited:
                        continue

                    ele = grid[nr][nc]

                    greater = max(curr_time, ele)

                    if greater < time[nr][nc]:
                        time[nr][nc] = greater

                        heapq.heappush(
                            heap,
                            (greater, nr, nc)
                        )