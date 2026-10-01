class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        '''
        At every index i, you have two choices:

        1. Don't use s[i] in a dictionary word
        → count it as extra
        → 1 + dfs(i + 1)

        2. Use a dictionary word starting at i
        → try s[i:j]
        → dfs(j)
        
        '''
        n = len(s)
        book = set(dictionary)

        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 0

            #  s[i] is an extra character
            ans = 1 + dfs(i + 1)
            # take a dictionary word starting at i
            for j in range(i, n ):
                word = s[i:j+1]

                if word in book:
                    ans = min(ans, dfs(j+1))

            return ans

        return dfs(0)