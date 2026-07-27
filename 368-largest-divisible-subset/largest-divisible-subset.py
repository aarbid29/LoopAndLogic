class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        n = len(nums)
        dp = [[nums[i]] for i in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] % nums[i] == 0:
                    candidate = [nums[i]] + dp[j]

                    if len(candidate) > len(dp[i]):
                        dp[i] = candidate

        res = []
        for subset in dp:
            if len(subset) > len(res):
                res = subset

        return res