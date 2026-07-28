class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(i, j):
            minn = float('inf')
            found = False

            for k in cuts:
                if i < k < j:
                    found = True
                    left = dfs(i, k)
                    right = dfs(k, j)
                    cost = left + right + (j - i)
                    minn = min(minn, cost)
            if not found:
                return 0
            return minn
        return dfs(0, n)