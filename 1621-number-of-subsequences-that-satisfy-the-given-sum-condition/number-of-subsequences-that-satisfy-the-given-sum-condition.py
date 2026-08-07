class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        l = 0
        r = len(nums) - 1
        count = 0

        while l <= r:

            if nums[l] + nums[r] > target:
                r -= 1
                continue

            possibility = 2 ** (r - l)
            count += possibility
            l += 1

        return count % (10**9 + 7)