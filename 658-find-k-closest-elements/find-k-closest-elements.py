class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [] 

        for num in arr:
            diff = abs(x-num)
            heapq.heappush(heap,(diff,num))

        res = []
        for i in range(k):
            diff , num = heapq.heappop(heap)

            res.append(num)
        
        res.sort()
        return res





        