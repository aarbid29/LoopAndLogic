class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        n = len(str1)
        m = len(str2)

        memo = {}

        def dfs(i, j):
            if i >= n or j >= m:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if str1[i] == str2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1) + 1
            else:
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))

            return memo[(i, j)]

        return dfs(0, 0)
