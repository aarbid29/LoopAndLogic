class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestHistogram(heights):
            n = len(heights)

            pse = [-1] * n
            nse = [n] * n

            stack = []
            for i in range(n):
                while stack and heights[i] < heights[stack[-1]]:
                    top = stack.pop()
                    nse[top] = i
                stack.append(i)

            stack = []
            for i in range(n):
                while stack and heights[i] < heights[stack[-1]]:
                    stack.pop()

                if stack:
                    pse[i] = stack[-1]

                stack.append(i)

            max_area = 0

            for i in range(n):
                height = heights[i]
                width = nse[i] - pse[i] - 1
                area = height * width
                max_area = max(max_area, area)

            return max_area

        row = len(matrix)
        col = len(matrix[0])

        dp = [[0] * col for _ in range(row)]

        for j in range(col):
            dp[0][j] = int(matrix[0][j])

        for i in range(1, row):
            for j in range(col):
                if matrix[i][j] == "1":
                    dp[i][j] = dp[i-1][j] + 1
                else:
                    dp[i][j] = 0

        maxx = 0
        for arr in dp:
            maxx = max(maxx, largestHistogram(arr))

        return maxx