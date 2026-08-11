class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        alr_in_nums = set(nums)
        running_sum = 0
        prev = -1

        for num in nums:

            if prev == -1 or prev + 1 == num:
                running_sum += num
                prev = num
            else:
                break

        summ = running_sum

        while summ in alr_in_nums:
            summ += 1

        return summ