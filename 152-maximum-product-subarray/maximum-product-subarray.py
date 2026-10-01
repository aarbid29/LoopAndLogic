class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxpro = nums[0]
        minpro = nums[0]
        maxx =  nums[0]

        for num in nums[1:]:
            if num < 0:
                maxpro,minpro = minpro,maxpro
            maxpro = max(num, maxpro*num)
            minpro = min(num , minpro*num)

            maxx = max(maxx,maxpro)

        return maxx

        