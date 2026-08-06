class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n= len(hand)
        if n % groupSize !=0:
            return False
        mp = Counter(hand)

        minHeap = list(mp.keys())
        heapq.heapify(minHeap)

        while minHeap:
            small_element = minHeap[0]

            for i in range(small_element ,small_element +groupSize):
                
                if mp[i]==0:
                    return False
                mp[i]-=1

                if mp[i]==0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True

        
                



                    