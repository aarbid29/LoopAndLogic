class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        LIMIT = 1024
        dp = [[[-1] * LIMIT for _ in range(col)] for _ in range(row)]

        def dfs(r, c, xor):
            if r >= row or c >= col:
                return float("inf")

            xor ^= grid[r][c]

            if r == row - 1 and c == col - 1:
                return xor

            if dp[r][c][xor] != -1:
                return dp[r][c][xor]

            right = dfs(r, c + 1, xor)
            down = dfs(r + 1, c, xor)

            dp[r][c][xor] = min(right, down)
            return dp[r][c][xor]

        return dfs(0, 0, 0)