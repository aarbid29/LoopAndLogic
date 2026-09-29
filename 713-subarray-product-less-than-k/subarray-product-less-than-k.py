class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # mp = defaultdict(int)
        # mp[1]=1
        # runningproduct = 1
        # count = 0

        # for num in nums:

        #     runningproduct *= num

        #     needed = runningproduct//k

        #     if needed in mp:
                

        # return count
        l = 0
        count = 0
        prd = 1
        n = len(nums)

        for r in range(n):
            curr = nums[r]
            prd *= curr

            while l <= r and prd >= k:
                left = nums[l]
                prd //= left
                l += 1

            if prd < k:
                count += r - l + 1

        return count







        

        



         
        