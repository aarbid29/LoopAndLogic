class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:

        freq = Counter(nums)
        num = []
        for key ,value in freq.items():
            num.append(key)
        n = len(num)
        num.sort()

        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0

            skip = dfs(i + 1)

            if i + 1 < n and num[i + 1] == num[i] + 1:
                take = num[i] * freq[num[i]] + dfs(i + 2)
            else:
                take = num[i] * freq[num[i]] + dfs(i + 1)

            return max(take, skip)
        return dfs(0)









            