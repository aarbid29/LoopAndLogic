from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        @cache
        def dfs(i, j):
            if j == m:
                return 1
            if i == n:
                return 0

            if s[i] == t[j]:
                take = dfs(i + 1, j + 1)
                no_take = dfs(i + 1, j)
                return take + no_take
            else:
                return dfs(i + 1, j)

        return dfs(0, 0)