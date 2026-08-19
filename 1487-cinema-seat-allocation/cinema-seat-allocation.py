class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        adj = defaultdict(set)

        for row, seat in reservedSeats:
            adj[row].add(seat)

        count = (n - len(adj)) * 2

        for seats in adj.values():
            families = 0

            if not any(seat in seats for seat in range(2, 6)):
                families += 1

            if not any(seat in seats for seat in range(6, 10)):
                families += 1

            if families == 0:
                if not any(seat in seats for seat in range(4, 8)):
                    families = 1

            count += families

        return count