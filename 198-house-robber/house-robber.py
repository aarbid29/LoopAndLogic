class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1

        @lru_cache(None)
        def dfs(i, taken):
            if i > n:
                return 0
            if taken:
                return dfs(i + 1, False)

            take = nums[i] + dfs(i + 1, True)
            no_take = dfs(i + 1, False)

            return max(take, no_take)

        return dfs(0, False)