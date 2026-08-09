from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, m):
            can_take_upto = min(2 * m, len(piles) - i)
            maxx = float("-inf")
            summ = 0

            if i >= len(piles):
                return 0

            for x in range(1, can_take_upto + 1):
                summ += piles[i + x - 1]
                tmp = summ - dfs(i + x, max(m, x))
                maxx = max(maxx, tmp)

            return maxx

        total = sum(piles)
        diff = dfs(0, 1)

        return (total + diff) // 2