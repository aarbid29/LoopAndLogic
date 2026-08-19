class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [[float("inf")] * n for _ in range(n + 1)]
        distance[src][0] = 0

        heap = []
        heapq.heappush(heap, (0, src))

        adj = defaultdict(list)

        for fromm, to, price in flights:
            adj[fromm].append((to, price))

        max_flights = min(k + 1, n - 1)

        while heap:
            stop, node = heapq.heappop(heap)

            if stop >= max_flights:
                continue

            for neigh, weight in adj[node]:
                new_cost = distance[node][stop] + weight

                if new_cost < distance[neigh][stop + 1]:
                    distance[neigh][stop + 1] = new_cost
                    heapq.heappush(heap, (stop + 1, neigh))

        ans = min(distance[dst])

        if ans == float("inf"):
            return -1

        return ans