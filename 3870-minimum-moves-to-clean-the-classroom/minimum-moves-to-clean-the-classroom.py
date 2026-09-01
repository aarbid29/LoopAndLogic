from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        rows = len(classroom)
        cols = len(classroom[0])

        litter_id = {}
        litter_count = 0
        start_r = start_c = 0

        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = litter_count
                    litter_count += 1

        target = (1 << litter_count) - 1

        dq = deque()
        dq.append((start_r, start_c, energy, 0, 0))

        best = {(start_r, start_c, 0): energy}

        while dq:
            r, c, e, mask, moves = dq.popleft()

            if mask == target:
                return moves

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                new_energy = e - 1

                if new_energy < 0:
                    continue

                new_mask = mask

                if classroom[nr][nc] == 'L':
                    bit = litter_id[(nr, nc)]
                    new_mask |= (1 << bit)

                if classroom[nr][nc] == 'R':
                    new_energy = energy

                key = (nr, nc, new_mask)

                if key in best and best[key] >= new_energy:
                    continue

                best[key] = new_energy
                dq.append((nr, nc, new_energy, new_mask, moves + 1))

        return -1