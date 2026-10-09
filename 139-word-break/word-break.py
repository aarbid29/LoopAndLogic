class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dictt = set(wordDict)
        @lru_cache(None)
        def dfs(i,subs):
            if i == n:
                return subs==""

            newsubs = subs+s[i]
            t2 = dfs(i+1,newsubs)
            t1 = False
            if newsubs in dictt:
                t1 = dfs(i+1 ,"")

            return t1 or t2

        return dfs(0,"")

            
                









        