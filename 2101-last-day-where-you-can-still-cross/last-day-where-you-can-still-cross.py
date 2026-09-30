from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def can_cross(day):
            water = set()

            for i in range(day):
                r, c = cells[i]
                water.add((r - 1, c - 1))

            dq = deque()
            visited = set()

            for c in range(col):
                if (0, c) not in water:
                    dq.append((0, c))
                    visited.add((0, c))

            while dq:
                r, c = dq.popleft()

                if r == row - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < row and 0 <= nc < col):
                        continue

                    if (nr, nc) in water:
                        continue

                    if (nr, nc) in visited:
                        continue

                    visited.add((nr, nc))
                    dq.append((nr, nc))

            return False

        left = 0
        right = len(cells)

        while left <= right:
            mid = (left + right) // 2

            if can_cross(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right