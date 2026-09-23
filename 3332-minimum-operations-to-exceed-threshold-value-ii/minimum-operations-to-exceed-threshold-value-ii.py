class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        #in a list , or AT A TIME 
        #
        heapq.heapify(nums)

        #ill just stop/break from the loop is the peek'd element is greater than or equal to k

        op = 0

        while nums:

            if nums[0]>= k or len(nums)<2:
                return op
            else:
                op+=1
                a = heapq.heappop(nums)
                b = heapq.heappop(nums)

                heapq.heappush(nums, a * 2 + b)
        
        





        