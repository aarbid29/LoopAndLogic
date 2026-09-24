class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, number in enumerate(nums):
            total = 0

            for digit in str(number):
                total += int(digit)

            if total == i:
                return i

        return -1
