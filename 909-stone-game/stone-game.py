from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n= len(piles)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(len(piles)-1,-1,-1):
            for j in range(len(piles)):
                if i < 0 or j >= len(piles) or i == j or i > j:
                    dp[i][j] = 0 
                dp[i][j] = max(piles[i]+dp[i+1][j],
                                piles[j]+dp[i][j-1])

        if dp[0][0] > sum(piles)-dp[0][0]:
            return True
        else:
            return False

        




