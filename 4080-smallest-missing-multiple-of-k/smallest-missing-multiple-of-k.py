class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        sett = set(nums)
        listt = []
        ans = k
        listt = []

        for i in range(1, len(nums) +2):
            listt.append(i * k)

        for multiple in listt:
            if multiple in sett:
                continue
            return multiple
        






        