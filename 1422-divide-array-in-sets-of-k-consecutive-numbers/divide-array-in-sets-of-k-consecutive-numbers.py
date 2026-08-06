class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n= len(nums)
        if n % k !=0:
            return False
        mp = Counter(nums)

        minHeap = list(mp.keys())
        heapq.heapify(minHeap)

        while minHeap:
            small_element = minHeap[0]

            for i in range(small_element ,small_element +k):
                
                if mp[i]==0:
                    return False
                mp[i]-=1

                if mp[i]==0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True

        