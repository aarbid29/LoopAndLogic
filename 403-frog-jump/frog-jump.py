class Solution:
    def canCross(self, stones: list[int]) -> bool:
        n = len(stones)

        stone = set(stones)

        

        @lru_cache(None)
        def dfs(i ,jump):
            if i == n-1:
                return True

            for nextjump in (jump-1,jump,jump+1):
                if nextjump <= 0:
                    continue

                can_do = stones[i]+ nextjump

                if can_do in stone:
                    j = stones.index(can_do)
                    if dfs(j , nextjump):
                        return True
            
            return False
        return dfs(0,0)
        