class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_map = {}
        for i in range(len(points)):
            adj_map[i] = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                distance = abs(x1 - x2) + abs(y1 - y2)

                adj_map[i].append((j, distance))
                adj_map[j].append((i, distance))
        heap = []
        heapq.heappush(heap,(0,0))
        visited = set()
        add = 0

        while heap:
            wei, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            add += wei

            for nodee, value in adj_map[node]:
                if nodee not in visited:
                    heapq.heappush(heap, (value, nodee))

        
        return add








