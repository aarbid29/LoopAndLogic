class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = set()
        res = []
        n = len(nums)

        def backtrack(sol):
            if len(sol) == n:
                res.append(sol[:])
                return

            for i in range(n):
                if i in used:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and i - 1 not in used:
                    continue

                used.add(i)
                sol.append(nums[i])

                backtrack(sol)

                sol.pop()
                used.remove(i)

        backtrack([])
        return res