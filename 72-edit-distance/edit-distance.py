from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        @cache
        def dfs(i, j):
            if i == n:
                return m - j
            if j == m:
                return n - i

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            insert = dfs(i, j + 1) + 1
            delete = dfs(i + 1, j) + 1
            replace = dfs(i + 1, j + 1) + 1

            return min(insert, delete, replace)

        return dfs(0, 0)