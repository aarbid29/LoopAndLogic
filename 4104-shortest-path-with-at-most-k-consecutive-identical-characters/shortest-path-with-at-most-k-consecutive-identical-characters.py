class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = defaultdict(list)
        for a, b, w in edges:
            adj[a].append((b, w))

        heap = []
        best = {}

        # (weight, node, last_char, count)
        heapq.heappush(heap, (0, 0, labels[0], 1))

        best[(0, labels[0], 1)] = 0

        while heap:
            weight, node, last_char, count = heapq.heappop(heap)

            if weight > best[(node, last_char, count)]:
                continue

            if node == n - 1:
                return weight

            for neigh, val in adj[node]:

                if labels[neigh] == last_char:
                    new_count = count + 1
                    new_last_char = last_char
                else:
                    new_count = 1
                    new_last_char = labels[neigh]

                if new_count > k:
                    continue

                newweight = weight + val

                state = (neigh, new_last_char, new_count)

                if newweight < best.get(state, float("inf")):
                    best[state] = newweight
                    heapq.heappush(
                        heap,
                        (newweight, neigh, new_last_char, new_count)
                    )

        return -1