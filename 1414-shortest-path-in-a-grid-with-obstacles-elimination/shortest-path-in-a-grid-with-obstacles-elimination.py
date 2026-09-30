class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row = len(grid)
        col = len(grid[0])

        best = defaultdict(dict)
        best[(0, 0)][0] = 0

        heap = []
        heapq.heappush(heap, (0, 0, 0, 0))
        # steps, destruct, r, c

        while heap:

            steps, destruct, r, c = heapq.heappop(heap)

            if r == row - 1 and c == col - 1:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < row and 0 <= nc < col):
                    continue

                if grid[nr][nc] == 0:

                    if destruct not in best[(nr, nc)] or best[(nr, nc)][destruct] > steps + 1:
                        best[(nr, nc)][destruct] = steps + 1
                        heapq.heappush(
                            heap,
                            (steps + 1, destruct, nr, nc)
                        )

                if grid[nr][nc] == 1:

                    newdes = destruct + 1

                    if newdes > k:
                        continue

                    if newdes not in best[(nr, nc)] or best[(nr, nc)][newdes] > steps + 1:
                        best[(nr, nc)][newdes] = steps + 1
                        heapq.heappush(
                            heap,
                            (steps + 1, newdes, nr, nc)
                        )

        return -1