class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}

        def dfs(summ):
            if summ == target:
                return 1

            if summ > target:
                return 0

            if summ in memo:
                return memo[summ]

            count = 0

            for num in nums:
                count += dfs(summ + num)

            memo[summ] = count
            return count

        return dfs(0)