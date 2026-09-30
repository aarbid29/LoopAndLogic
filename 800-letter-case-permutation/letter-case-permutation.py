class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:

        res = []
        n = len(s)
        @lru_cache(None)
        def dfs(i,strr):
            if i==n:
                res.append(strr)
                return 
            if s[i].isalpha():
                #upper make 
                if s[i].isupper():
                    dfs(i+1,strr+s[i].lower())
                    dfs(i+1,strr+s[i])
                else:
                    dfs(i+1,strr+s[i].upper())
                    dfs(i+1,strr+s[i])

            else:
                dfs(i+1,strr+s[i])
 
            return 
        dfs(0 ,"")
        return res


        