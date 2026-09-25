class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        heap = []
        l = 0
        track = 0
        res = []
        stale = set()
        for r in range(len(nums)):
            heapq.heappush(heap,(-nums[r],r))
            track+=1

            while track>k:
                left = nums[l]
                stale.add(l)
                l+=1
                track-=1
            
            while heap[0][1] in stale:
                stale.remove(heap[0][1])
                heapq.heappop(heap)
            if track==k:
                maxx,idx = heap[0]
                res.append(-maxx)
        
        return res


        