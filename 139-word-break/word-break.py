class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        book = set(wordDict)
        n = len(s)
        @lru_cache(None)
        def dfs(i):
            if i == n:
                return True

            #skip curr charater :
            
            for j in range(i,n):
                new = s[i:j+1]

                if new in book:
                    if dfs(j+1):
                        return True
            return False
        
        return dfs(0)




        