class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        max_dq = deque()
        min_dq = deque()
        maxx = 0

        for r in range(len(nums)):
            curr = nums[r]

            while max_dq and max_dq[-1] < curr:
                max_dq.pop()
            max_dq.append(curr)

            while min_dq and min_dq[-1] > curr:
                min_dq.pop()
            min_dq.append(curr)

            while max_dq[0] - min_dq[0] > limit:
                if nums[l] == max_dq[0]:
                    max_dq.popleft()

                if nums[l] == min_dq[0]:
                    min_dq.popleft()

                l += 1

            maxx = max(maxx, r - l + 1)

        return maxx