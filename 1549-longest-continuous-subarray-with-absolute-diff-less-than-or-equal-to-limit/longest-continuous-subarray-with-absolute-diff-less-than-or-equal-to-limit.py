class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        count = 0 
        #i can traverse from 8 to 7 , but how to start subarray and check for it from 2 to 7 , then 4 to 7 then 7 itself
        max_dq = deque()#max ele in front
        min_dq = deque()#min ele in front
        maxx = 0 # for max length
        l =0 

        for r in range(len(nums)):
            curr = nums[r]
            while max_dq and curr > max_dq[-1]:
                max_dq.pop()
            max_dq.append(curr)

            while min_dq and curr < min_dq[-1]:
                min_dq.pop() #as min_dp[-1]has alr been processed as itself as the min
            min_dq.append(curr)
            
            while max_dq[0] - min_dq[0] > limit:
                left = nums[l]

                if left == max_dq[0]:
                    max_dq.popleft()
                
                if left == min_dq[0]:
                    min_dq.popleft()
                l+=1
            
            maxx = max(maxx,r-l+1)
        return maxx








        