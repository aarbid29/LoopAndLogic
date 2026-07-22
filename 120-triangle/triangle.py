class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)
        dp = [[None] * n for _ in range(n)]

        def dfs(r, c):
            if r == n - 1:
                return triangle[r][c]

            if dp[r][c] is not None:
                return dp[r][c]

            left = dfs(r + 1, c)
            right = dfs(r + 1, c + 1)

            dp[r][c] = min(left, right) + triangle[r][c]

            return dp[r][c]

        return dfs(0, 0)