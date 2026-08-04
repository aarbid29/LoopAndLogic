from functools import lru_cache
class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def dfs(x):
            if x==1 :
                return 1
            ans = 0
            maxx = 0
            for i in range(1,x+1):
                ans = i* max(x-i,dfs(x-i))
                maxx = max(maxx,ans)
            return maxx
        
        return dfs(n)
        