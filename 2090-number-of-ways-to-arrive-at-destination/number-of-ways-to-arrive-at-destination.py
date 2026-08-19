class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        adj = defaultdict(list)

        for fromm, to, time in roads:
            adj[fromm].append((to, time))
            adj[to].append((fromm, time))

        distance = [float("inf")] * n
        ways = [0] * n

        distance[0] = 0
        ways[0] = 1

        heap = []
        heapq.heappush(heap, (0, 0))

        while heap:
            val, node = heapq.heappop(heap)

            if val > distance[node]:
                continue

            for neigh, weight in adj[node]:
                new_distance = val + weight

                if new_distance < distance[neigh]:
                    distance[neigh] = new_distance
                    ways[neigh] = ways[node] % MOD

                    heapq.heappush(heap, (new_distance, neigh))

                elif new_distance == distance[neigh]:
                    ways[neigh] = (ways[neigh] + ways[node]) % MOD

        return ways[n - 1]