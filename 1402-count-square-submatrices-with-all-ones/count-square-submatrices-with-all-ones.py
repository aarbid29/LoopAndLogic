class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        mp = collections.defaultdict(int)

        dp = [[0]* col for _ in range(row)]

        for j in range(col):
            dp[0][j] = matrix[0][j]
        for i in range(row):
            dp[i][0] = matrix[i][0]

        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==0:
                    dp[i][j]=0
                    continue
                dp[i][j]  = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1

        total = 0
        for i in range(row):
            for j in range(col):
                if dp[i][j]==0:
                    continue
                total+=dp[i][j]

        return total
                

                





        



        