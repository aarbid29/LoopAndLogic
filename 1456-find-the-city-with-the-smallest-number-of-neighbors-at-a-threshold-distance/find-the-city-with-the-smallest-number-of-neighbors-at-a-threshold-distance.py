class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        mp = defaultdict(int)

        for fromm, to, weight in edges:
            adj[fromm].append((to, weight))
            adj[to].append((fromm, weight))

        def can_reach(parent):
            dist = [float("inf")] * n
            dist[parent] = 0

            heap = [(0, parent)]

            while heap:
                val, node = heapq.heappop(heap)

                if val > dist[node]:
                    continue

                for neigh, weight in adj[node]:
                    new_dist = val + weight

                    if new_dist < dist[neigh]:
                        dist[neigh] = new_dist
                        heapq.heappush(heap, (new_dist, neigh))
            
            mp[parent] = sum(d <= distanceThreshold for d in dist)-1

        for i in range(n):
            can_reach(i)

        return min(mp, key=lambda k: (mp[k], -k))