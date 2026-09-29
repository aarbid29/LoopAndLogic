class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])
        heap = []
        cap = 0
        for pasen , start ,end in trips:

            while heap and heap[0][0]<= start:
                e,s,p = heapq.heappop(heap)
                cap-= p

            cap+= pasen

            if cap>capacity:
                return False
            
            heapq.heappush(heap,(end,start,pasen))
        
        return True




            









        