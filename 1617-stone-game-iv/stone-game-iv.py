class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dfs(n):
            if n == 0:
                return True

            res = False

            for i in range(1, math.isqrt(n) + 1):
                take = i * i

                output = dfs(n - take)
                res = res or output

            return not res

        return not dfs(n)