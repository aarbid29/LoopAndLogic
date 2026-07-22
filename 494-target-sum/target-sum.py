class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mp = {}

        def dfs(i, total):
            if i == n:
                return 1 if total == target else 0

            if (i, total) in mp:
                return mp[(i, total)]

            take_as_is = dfs(i+1, total + nums[i])
            negative_it = dfs(i+1, total - nums[i])

            mp[(i, total)] = take_as_is + negative_it

            return mp[(i, total)]

        return dfs(0, 0)