class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

        visited = set()
        visited.add((0, 0))

        dq = deque([(0, 0)])
        level = 1

        while dq:
            for _ in range(len(dq)):
                r, c = dq.popleft()

                if r == rows - 1 and c == cols - 1:
                    return level

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 0 and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            dq.append((nr, nc))

            level += 1

        return -1