from functools import lru_cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(step):
            if step == len(nums) - 1:
                return True
            if step >= len(nums):
                return False

            for i in range(1, nums[step] + 1):
                if dfs(step + i):
                    return True
            
            return False

        return dfs(0)