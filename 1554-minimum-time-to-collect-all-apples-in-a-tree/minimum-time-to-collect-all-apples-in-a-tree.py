class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        adj = defaultdict(list)
        for src, neigh in edges:
            adj[src].append(neigh)
            adj[neigh].append(src)
        def dfs(node, parent):
            ans = 0
            for neigh in adj[node]:
                if neigh == parent:
                    continue

                child = dfs(neigh, node)

                if child > 0 or hasApple[neigh]:
                    ans += child + 2

            return ans

        return dfs(0, -1)