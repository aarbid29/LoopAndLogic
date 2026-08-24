class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][amount] = 1

        for i in range(n - 1, -1, -1):
            for summ in range(amount - 1, -1, -1):

                take = 0
                if summ + coins[i] <= amount:
                    take = dp[i][summ + coins[i]]

                no_take = dp[i + 1][summ]

                dp[i][summ] = take + no_take

        return dp[0][0]