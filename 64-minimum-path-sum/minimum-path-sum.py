class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):

                if r == m - 1 and c == n - 1:
                    dp[r][c] = grid[r][c]
                    continue

                down = dp[r + 1][c] if r + 1 < m else float('inf')
                right = dp[r][c + 1] if c + 1 < n else float('inf')

                dp[r][c] = grid[r][c] + min(down, right)

        return dp[0][0]