class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        n = len(graph)

        target = (1 << n) - 1

        dq = deque()
        visited = set()

        for i in range(n):
            mask = 1 << i
            dq.append((i, 0, mask))

        while dq:
            node, distance, mask = dq.popleft()

            if mask == target:
                return distance

            for neigh in graph[node]:

                new_mask = mask | (1 << neigh)
                new_distance = distance + 1

                state = (neigh, new_mask)

                if state in visited:
                    continue
                visited.add(state)
                dq.append((neigh, new_distance, new_mask))