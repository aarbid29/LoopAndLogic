class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def solve(k):
            l = 0
            mp = defaultdict(int)
            count = 0
            arr = 0

            for r in range(len(nums)):
                curr = nums[r]

                if curr not in mp:
                    count += 1

                mp[curr] += 1

                while count > k:
                    left = nums[l]
                    mp[left] -= 1
                    l += 1

                    if mp[left] == 0:
                        del mp[left]
                        count -= 1

                arr += r - l + 1

            return arr

        return solve(k) - solve(k - 1)