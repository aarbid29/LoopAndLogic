from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def is_all_stars(j):
            if j < 0:
                return True
            if p[j] != '*':
                return False
            return is_all_stars(j - 1)

        @cache
        def solve(i, j):
            if i < 0 and j < 0:
                return True

            if i >= 0 and j < 0:
                return False

            if i < 0 and j >= 0:
                return is_all_stars(j)

            if s[i] == p[j] or p[j] == '?':
                return solve(i - 1, j - 1)

            if p[j] == '*':
                return solve(i - 1, j) or solve(i, j - 1)

            return False

        return solve(len(s) - 1, len(p) - 1)