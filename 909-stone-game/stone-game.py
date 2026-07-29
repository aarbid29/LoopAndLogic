from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @lru_cache(None)
        def dfs(i,j):
            if i < 0 or j >= len(piles) or i == j or i > j:
                return 0 


            left = piles[i]
            right = piles[j]


            take_left = left + dfs(i+1,j)
            take_right = right + dfs(i,j-1)

            return max(take_left,take_right)

        ans = dfs(0,len(piles)-1)
        total = sum(piles)

        if ans>total-ans:
            return True 
        else:
            return False