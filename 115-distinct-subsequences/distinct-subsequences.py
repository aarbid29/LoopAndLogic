class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m= len(s)
        n = len(t)
        count = 0 
        @lru_cache(None)
        def dfs(i,j):
            #i,j means im currently checking those indices on s and t 
            if i >=m and j>=n:
                return 1 
                
            if i>=m and j<n:
                return 0

            if j == n:
                return 1 

            #if matched , we have two possibilites , take or no_take curr i
            if s[i]==t[j]:
                return dfs(i+1,j) + dfs(i+1,j+1)
            else:
                return dfs(i+1,j)
            

        
        return dfs(0,0)
            

        