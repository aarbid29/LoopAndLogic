class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N1, N2 = len(str1), len(str2)

        @cache
        def dp(i, j):
            if i == N1:
                return N2 - j
            if j == N2:
                return N1 - i
            if str1[i] == str2[j]:
                return 1 + dp(i + 1, j + 1)
            else:
                return 1 + min(dp(i + 1, j), dp(i, j + 1))
        
        @cache
        def rec(i, j):
            if i == N1:
                return str2[j:]
            if j == N2:
                return str1[i:]
            if str1[i] == str2[j]:
                return str1[i] + rec(i + 1, j + 1)
            else:
                if dp(i + 1, j) < dp(i, j + 1):
                    return str1[i] + rec(i + 1, j)
                else:
                    return str2[j] + rec(i, j + 1)
        
        return rec(0, 0)        