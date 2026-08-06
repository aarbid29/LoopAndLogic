class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)

        if len(hand) % groupSize != 0:
            return False

        heap = list(freq.keys())
        heapq.heapify(heap)

        while heap:
            small_element = heap[0]

            for val in range(small_element, small_element + groupSize):
                if val not in freq or freq[val] == 0:
                    return False

                freq[val] -= 1

                if freq[val] == 0:
                    heapq.heappop(heap)

        return True