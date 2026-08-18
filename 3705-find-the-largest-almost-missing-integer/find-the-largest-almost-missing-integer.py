class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)

        for i in range(len(nums) - k + 1):
            for x in set(nums[i:i+k]):
                freq[x] += 1

        ans = -1

        for x in freq:
            if freq[x] == 1:
                ans = max(ans, x)

        return ans