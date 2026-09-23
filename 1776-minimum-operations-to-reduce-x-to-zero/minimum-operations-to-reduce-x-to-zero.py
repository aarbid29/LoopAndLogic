class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        xmin = min(nums)
        if xmin > x:
            return -1
        
        
        summ = sum(nums)
        if summ < x:
            return -1
        n = len(nums)

        needed = summ - x
        #so we need a subarray of sum needed
        l = 0 
        runningsum = 0
        minn = float("inf")
        for r in range(len(nums)):
            curr = nums[r]
            while  runningsum + curr > needed:
                left = nums[l]
                runningsum-=left
                l+=1
            runningsum+= curr
            if runningsum == needed:
                lenght = r-l+1
                diff = n -lenght
                minn = min(minn , diff)
        
        if minn != float("inf"):
            return minn
        else:
            return -1


            

            


