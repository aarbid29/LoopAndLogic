class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

        dp = [[0] * col for _ in range(row)]

        for j in range(col):
            dp[0][j] = int(matrix[0][j])

        for i in range(row):
            dp[i][0] = int(matrix[i][0])

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                    continue

                dp[i][j] = min(
                    dp[i][j-1],
                    dp[i-1][j],
                    dp[i-1][j-1]
                ) + 1

        max_side = max(max(row) for row in dp)

        return max_side ** 2