class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        heap = []
        heapq.heappush(heap, (0, k))

        adj = defaultdict(list)

        for u, v, weight in times:
            adj[u].append((weight, v))

        time = [float("inf")] * (n + 1)
        time[k] = 0

        while heap:
            val, node = heapq.heappop(heap)

            for weight, neigh in adj[node]:
                
                if val + weight < time[neigh]:
                    time[neigh] = val + weight
                    heapq.heappush(heap, (time[neigh], neigh))

        if float("inf") in time[1:]:
            return -1

        return max(time[1:])