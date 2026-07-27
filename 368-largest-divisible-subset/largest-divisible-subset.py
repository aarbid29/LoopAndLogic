class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        dp = [ [] for _ in range(len(nums)+1)]
        n = len(nums)

        for i in range(n-1, -1, -1):
            res = [nums[i]]
            for j in range(i+1, n):
                if nums[j]% nums[i] == 0 :
                    tmp = [nums[i]] + dp[j]
                    if len(tmp)> len(res):
                        res = tmp
            dp[i] = res
        return max(dp,key = len)

