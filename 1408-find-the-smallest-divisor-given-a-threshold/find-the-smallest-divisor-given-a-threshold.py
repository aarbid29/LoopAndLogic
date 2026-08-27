class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)

        while l < r:
            midd = (l + r) // 2

            thres = 0
            for num in nums:
                thres += ceil(num / midd)

            if thres > threshold:
                l = midd + 1
            else:
                r = midd

        return l