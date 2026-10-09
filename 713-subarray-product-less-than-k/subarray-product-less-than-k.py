class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        l = 0 

        count = 0 
        runningproduct =1 

        for r in range(len(nums)):
            runningproduct*=nums[r]


            while l < r and runningproduct > k:
                left = nums[l]
                runningproduct/= left
                l+=1
            if runningproduct < k:
                count+= (r-l+1)
        return count

        