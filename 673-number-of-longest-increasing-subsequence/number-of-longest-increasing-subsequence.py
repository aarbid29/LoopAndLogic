class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp_len = [1 for _ in range(n)]
        dp_count = [1 for _ in range(n)]

        for i in range(n - 1, -1, -1):
            maxx = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    tmp = dp_len[j] + 1
                    maxx = max(tmp, maxx)
            dp_len[i] = maxx

        for i in range(n - 1, -1, -1):
            dp_count[i] = 1 if dp_len[i] == 1 else 0
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    if dp_len[i] == dp_len[j] + 1:
                        dp_count[i] += dp_count[j]

        longest = max(dp_len)
        ans = 0
        for i in range(n):
            if dp_len[i] == longest:
                ans += dp_count[i]

        return ans