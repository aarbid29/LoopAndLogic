class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dictt = set(wordDict)
        @lru_cache(None)
        def dfs(i):
            if i == n:
                return True

            for j in range(i,n):
                
                new = s[i:j+1]

                if new in dictt:
                    if dfs(j+1):
                        return True
            return False

        return dfs(0)
        