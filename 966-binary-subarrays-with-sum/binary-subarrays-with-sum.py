class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        mp = defaultdict(int)

        runningsum = 0 
        prefix = 0 
        count = 0 
        mp[0] = 1

        for num in nums:
            runningsum += num
            prefix = runningsum -  goal 

            if prefix in mp:
                count+= mp[prefix]
            mp[runningsum] = mp.get(runningsum,0)+1
        

        return count 
        