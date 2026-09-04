class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_mp ={}
        #max calculate at each distance 
        maxx = float("-inf")
        l = 0 
        for r in range(len(nums)):
            maxx = max(maxx,nums[r])
            max_mp[(l,r)] = maxx
        
        #min calculate at each distance 
        minn = float("inf")
        min_mp = {}
        last = n-1
        for r in range(len(nums)-1,-1,-1):
            minn = min(minn,nums[r])
            min_mp[(r,last)] = minn
        
        minn = -1
        for i in range(len(nums)):
            left = max_mp[(0, i)]
            right = min_mp[(i, last)]
            calc = left - right
            if calc <= k:
                return i
        return minn

        
        






        




        