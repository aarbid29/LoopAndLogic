class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @lru_cache(None)
        def dfs(i, transaction, bought):
            if i >= len(prices):
                return 0

            if transaction >= k and bought:
                return 0

            if bought:
                profit = max(
                    -prices[i] + dfs(i + 1, transaction, 0),  
                    dfs(i + 1, transaction, 1)                  
                )
            else:
                profit = max(
                    prices[i] + dfs(i + 1, transaction + 1, 1),  
                    dfs(i + 1, transaction, 0)                  
                )

            return profit

        ans = dfs(0, 0, 1)
        dfs.cache_clear()
        return ans
        