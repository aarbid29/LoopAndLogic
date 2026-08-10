class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count= 0
        res = []
        l =0
        for r in range(len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            count += 1

            if count >= k:
                while heap[0][1] < l:
                    heapq.heappop(heap)

                res.append(-heap[0][0])
                l += 1
                count -= 1

        return res






        