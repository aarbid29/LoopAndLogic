class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dfs(i,summ):
            if summ == amount:
                return 1 
            if summ>amount:
                return 0
            if i >=len(coins):
                return 0

            add =  dfs(i,summ+coins[i]) + dfs(i+1,summ)
            return add

        return dfs(0,0)

    

