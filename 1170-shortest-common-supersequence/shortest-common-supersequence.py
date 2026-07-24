class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str):

        m = len(str1)
        n = len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            dp[i][n] = m - i

        for j in range(n - 1, -1, -1):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])

        ans = []
        i = j = 0

        while i < m and j < n:
            if str1[i] == str2[j]:
                ans.append(str1[i])
                i += 1
                j += 1

            elif dp[i + 1][j] <= dp[i][j + 1]:
                ans.append(str1[i])
                i += 1

            else:
                ans.append(str2[j])
                j += 1

        while i < m:
            ans.append(str1[i])
            i += 1

        while j < n:
            ans.append(str2[j])
            j += 1

        return "".join(ans)