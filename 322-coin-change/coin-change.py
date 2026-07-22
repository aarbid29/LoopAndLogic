class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(i, summ):
            if summ == amount:
                return 0

            if summ > amount:
                return float("inf")

            if i == len(coins):
                return float("inf")

            if (i, summ) in memo:
                return memo[(i, summ)]

            no_take = dfs(i + 1, summ)

            take = 1 + dfs(i, summ + coins[i])

            memo[(i, summ)] = min(no_take, take)
            return memo[(i, summ)]

        ans = dfs(0, 0)

        return -1 if ans == float("inf") else ans