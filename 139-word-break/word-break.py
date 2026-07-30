from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        mp = defaultdict(list)
        for word in wordDict:
            mp[word[0]].append(word)
        @lru_cache(None)
        def dfs(i):
            if i == len(s):
                return True

            if s[i] in mp:
                for word in mp[s[i]]:
                    n = len(word)

                    if s[i:i+n] == word:
                        if dfs(i + n):
                            return True
                        

            return False
        return dfs(0)