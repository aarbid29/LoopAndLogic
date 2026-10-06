class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i, rem):
            if i == n:
                return 0 if rem == 0 else float("-inf")

            skip = dfs(i + 1, rem)

            take = nums[i] + dfs(i + 1, (rem + nums[i]) % 3)

            return max(skip, take)

        return dfs(0, 0)
