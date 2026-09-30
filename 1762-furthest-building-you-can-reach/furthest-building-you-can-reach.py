class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:

        heap = []
        n = len(heights)

        for i in range(1, n):
            diff = heights[i] - heights[i - 1]

            if diff <= 0:
                continue

            bricks -= diff
            heapq.heappush(heap, -diff)

            if bricks < 0:
                if ladders == 0:
                    return i - 1

                ladders -= 1
                bricks += -heapq.heappop(heap)

        return n - 1