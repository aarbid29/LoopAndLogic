class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        xmin = min(nums)
        if xmin > x:
            return -1
        l = 0
        n = len(nums)
        total = sum(nums)
        if total < x:
            return -1
        mp = defaultdict(int)
        mp[0]=1
        op = -1
        summ = sum(nums)
        runningsum = 0   
        length = float("inf")

        for r in range(len(nums)):
            runningsum+= nums[r]

            while l< n and total - runningsum < x:
                left =nums[l]
                runningsum -= left
                l+=1
            
            if total-runningsum==x:
                length = min(length , n- (r-l+1))
        if length != float("inf"):
            return length
        else:
            return -1

        