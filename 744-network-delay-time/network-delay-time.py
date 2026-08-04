class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)
        distance = [float("inf") for _ in range(n + 1)]
        distance[k] = 0

        for u, v, w in times:
            adj[u].append((v, w))

        heap = []
        heapq.heappush(heap, (0, k))

        while heap:
            weight, node = heapq.heappop(heap)
            for neigh, val in adj[node]:
                if distance[node] + val < distance[neigh]:
                    distance[neigh] = distance[node] + val
                    heapq.heappush(heap, (distance[neigh], neigh))

        if float("inf") in distance[1:]:
            return -1
        return max(distance[1:])