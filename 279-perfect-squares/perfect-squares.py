from functools import lru_cache

class Solution:
    def numSquares(self, n: int) -> int:

        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        @lru_cache(None)
        def dfs(total):
            if total == n:
                return 0

            if total > n:
                return float('inf')

            ans = float('inf')

            for square in squares:
                ans = min(ans, 1 + dfs(total + square))

            return ans

        return dfs(0)