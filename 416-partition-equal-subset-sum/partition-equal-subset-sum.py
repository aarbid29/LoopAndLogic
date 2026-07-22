class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        needed = total // 2

        @lru_cache(None)
        def dfs(i, rem):
            if rem == 0:
                return True

            if rem < 0 or i >= len(nums):
                return False

            return dfs(i + 1, rem - nums[i]) or dfs(i + 1, rem)

        return dfs(0, needed)