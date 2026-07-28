class Solution:
    def climbStairs(self, n: int) -> int:
        # def dfs(i):
        #     if i > n:
        #         return 0
        #     if i == n:
        #         return 1
        #     two_step =  dfs(i+2)
        #     one_step =  dfs(i+1)

        #     return two_step+one_step

        
        # return dfs(0)
        dp = [0] * (n + 2)
        dp[n] = 1 
        for i in range(n-1,-1,-1):
            dp[i] = dp[i+2] + dp[i+1]

        return dp[0]
        
        




            


        