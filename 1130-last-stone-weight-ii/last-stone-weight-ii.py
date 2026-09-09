class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summ = sum(stones)
        midd = ceil(summ+1/2)
        minn = float("inf")
        n = len(stones)
        @lru_cache(None)
        def dfs(i,weight):
            nonlocal minn
            if weight>=midd or i ==n:
                minn = min(minn ,abs(weight - (summ-weight)))
                return
            #take curr i 
            take = dfs(i+1, stones[i]+weight)

            no_take = dfs(i+1 ,weight)

            return
        dfs(0,0)
        return minn






            



        