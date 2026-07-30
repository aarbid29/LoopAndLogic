class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        # def dfs(r,c):
        #     if r== len(grid)-1 and c==len(grid[0])-1:
        #         return grid[r][c]

        #     if r >=row or c >= col:
        #         return float("inf")
        #     right = grid[r][c] +dfs(r,c+1)
        #     down = grid[r][c]+ dfs(r+1,c)

        #     return min(right,down)

        # return dfs(0,0)
        dp = [[float("inf") for _ in range(col + 1)] for _ in range(row + 1)]
        dp[row-1][col-1] = grid[row-1][col-1]

        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                if (r, c) == (row - 1, col - 1):
                    dp[row - 1][col - 1] = grid[row - 1][col - 1]
                    continue
                right = grid[r][c] + dp[r][c+1]
                down = grid[r][c]+ dp[r+1][c]

                dp[r][c] = min(right,down)
        
        return dp[0][0]

        




        