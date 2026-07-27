from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @lru_cache(None)
        def dfs(i):
            if i == len(nums):
                return 0

            ans = 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    ans = max(ans, 1 + dfs(j))

            return ans

        return max(dfs(i) for i in range(len(nums)))