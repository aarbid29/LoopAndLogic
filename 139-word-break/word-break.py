class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        dictionary = set(wordDict)
        count = 0 
        n = len(s)
        @lru_cache(None)
        def dfs(i ,substring):
            if i == n:
                return substring in dictionary or substring ==""

            substring+=s[i]

            build = dfs(i+1,substring)

            if substring in dictionary:
                new = dfs(i+1,"")
            else:
                new = False
            

            return new or build
            
        return dfs(0,"")















