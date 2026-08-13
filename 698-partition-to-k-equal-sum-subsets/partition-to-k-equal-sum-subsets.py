class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summ = sum(nums)

        if summ % k != 0:
            return False

        target = summ // k
        nums.sort(reverse=True)

        used = [False] * len(nums)

        def backtrack(start, total, groups):
            if groups == k:
                return True

            if total == target:
                return backtrack(0, 0, groups + 1)

            for i in range(start, len(nums)):
                if used[i]:
                    continue

                if i > start and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                if total + nums[i] > target:
                    continue

                used[i] = True

                if backtrack(i + 1, total + nums[i], groups):
                    return True

                used[i] = False

            return False

        return backtrack(0, 0, 0)