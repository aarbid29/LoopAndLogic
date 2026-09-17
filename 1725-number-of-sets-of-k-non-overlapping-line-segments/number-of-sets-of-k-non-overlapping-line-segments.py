class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        # @lru_cache(None)
        # def dfs(i, made):
        #     if made == k:
        #         return 1 
        #     if i >= n - 1:
        #         return 0
        #     #dont start segment at i
        #     skip = dfs(i + 1, made)
        #     #  start a segment at i and make the segment with j
        #     curr = 0
        #     for j in range(i + 1, n):
        #         curr += dfs(j, made + 1) # wher k is i+1 so in curr in bottom up
        #     return (curr + skip) % MOD
        # return dfs(0, 0) % MOD

        dp = [[0] * (k + 1) for _ in range(n)]
        for i in range(n): #the base of recursion
            dp[i][k] = 1

        for made in range(k-1,-1,-1):
            curr = 0 
            for i in range(n-2,-1,-1):
                #using i as the starting point and i+1 as the ending here
                skip = dp[i+1][made]
                curr += dp[i+1][made+1]

                dp[i][made] = (curr+skip )% MOD

        return dp[0][0]

