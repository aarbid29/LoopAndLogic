class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()

        mp =defaultdict(int)

        l = 0 
        maxx = 0
        running_sum = 0

        for r in range(len(nums)):
            curr = nums[r]
            running_sum+= curr

            while curr * (r - l + 1) - running_sum > k:
                running_sum -= nums[l]
                l+=1
                
            maxx = max(maxx ,r-l+1)


        return maxx
















        