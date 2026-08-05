from functools import lru_cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(step):
            if step == len(nums) - 1:
                return 0

            if step >= len(nums) or nums[step] == 0:
                return float("inf")

            ans = float("inf")

            for i in range(1, nums[step] + 1):
                ans = min(ans, 1 + dfs(step + i))

            return ans

        return dfs(0)