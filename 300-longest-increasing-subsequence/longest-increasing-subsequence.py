class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        dp  = [ 1 for _ in range(len(nums)+1)]
        for i in range(len(nums)-1,-1,-1):
            maxx =1
            for j in range(i+1,len(nums)):
                if nums[j]> nums[i]:
                    tmp = dp[j] +1
                    maxx = max(maxx,tmp)
            
            dp[i]= maxx
        return max(dp)

            












         
        