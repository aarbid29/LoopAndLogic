class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        n = len(graph)

        target = (1 << n) - 1

        dq = deque()
        best_distance = {}

        for i in range(n):
            mask = 1 << i
            dq.append((i, 0, mask))
            best_distance[(i, mask)] = 0

        while dq:
            node, distance, mask = dq.popleft()

            if mask == target:
                return distance

            for neigh in graph[node]:

                new_mask = mask | (1 << neigh)
                new_distance = distance + 1

                state = (neigh, new_mask)

                if state in best_distance:
                    continue

                best_distance[state] = new_distance
                dq.append((neigh, new_distance, new_mask))