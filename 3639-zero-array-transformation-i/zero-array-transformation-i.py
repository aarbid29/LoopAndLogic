class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        n = len(nums)
        res = [0]*n

        for start ,end in queries:
            res[start] -=1
            if end+1<n:
                res[end+1] +=1
        
        for i in range(1,n):
            res[i] = res[i-1]+res[i]
    

        for i in range(n):

            ans  = nums[i]+res[i]
            if ans > 0:
                return False
            nums[i]+=res[i]

        return True
        


        