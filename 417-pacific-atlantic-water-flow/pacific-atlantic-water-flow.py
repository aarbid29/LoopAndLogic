from collections import deque, defaultdict

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        row = len(heights)
        col = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacificdq = deque()
        atlanticdq = deque()
        res = []
        visited1 = set()
        visited2 = set()
        # canreach = defaultdict(list)
        canreach = defaultdict(lambda: [False, False])


        for r in range(row):
            for c in range(col):
                if c == 0 or r == 0:
                    pacificdq.append((r, c))
                    visited1.add((r, c))
                    canreach[(r, c)][0] = True

                if c == col - 1 or r == row - 1:
                    atlanticdq.append((r, c))
                    visited2.add((r, c))
                    canreach[(r, c)][1] = True

        while pacificdq:
            r, c = pacificdq.popleft()
            parent = heights[r][c]
            for dr, dc in directions:
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if not (0 <= nr < row and 0 <= nc < col) or (nr, nc) in visited1:
                        continue
                    neigh = heights[nr][nc]
                    if neigh >= parent:
                        canreach[(nr, nc)][0] = True
                        pacificdq.append((nr, nc))
                        visited1.add((nr, nc))

        while atlanticdq:
            r, c = atlanticdq.popleft()
            parent = heights[r][c]
            for dr, dc in directions:
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if not (0 <= nr < row and 0 <= nc < col) or (nr, nc) in visited2:
                        continue
                    neigh = heights[nr][nc]
                    if neigh >= parent:
                        canreach[(nr, nc)][1] = True
                        atlanticdq.append((nr, nc))
                        visited2.add((nr, nc))

        for r in range(row):
            for c in range(col):
                if canreach[(r, c)][0] and canreach[(r, c)][1]:
                    res.append([r, c])
                else:
                    b1 = False
                    b2 = False
                    parent = heights[r][c]
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if not (0 <= nr < row and 0 <= nc < col):
                            continue
                        child = heights[nr][nc]

                        if child <= parent:
                            if canreach[(nr, nc)][0]:
                                b1 = True
                            if canreach[(nr, nc)][1]:
                                b2 = True

                    if b1 and b2:
                        res.append([r, c])
                        continue

        return res
