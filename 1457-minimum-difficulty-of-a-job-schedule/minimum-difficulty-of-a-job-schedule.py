class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:

        if len(jobDifficulty)< d:
            return -1
        n = len(jobDifficulty)

        @lru_cache(None)
        def dfs(i , maxx,day):
            if i == n:
                return 0 if day == d else float("inf")

            if day == d:
                return float("inf")

            if n - i < d - day:
                return float("inf")
            #have two option at each i 
            #finish a day a  index i 
            # or skip it 

            maxx = max(maxx , jobDifficulty[i])
            skip = dfs(i+1 , maxx , day)

            take = maxx + dfs(i+1,0,day+1)


            return min(skip,take)

        
        return dfs(0,0,0)








        
        

        