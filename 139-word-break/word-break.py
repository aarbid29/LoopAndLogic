from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dictt = set(wordDict)

        @lru_cache(None)
        def dfs(i, string):
            if i == n:
                return string == ""

            new_substring = string + s[i]

            if new_substring in dictt:
                one = dfs(i + 1, "")
                two = dfs(i + 1, new_substring)

                return one or two
            else:
                return dfs(i + 1, new_substring)

        return dfs(0, "")