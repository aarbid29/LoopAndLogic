class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(summ):
            if summ == target:
                return 1

            if summ > target:
                return 0

            count = 0

            for num in nums:
                count += dfs(summ + num)

            return count

        return dfs(0)