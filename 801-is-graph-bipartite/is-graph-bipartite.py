class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        adj = defaultdict(list)
        for i, neighbors in enumerate(graph):
            adj[i] = neighbors[:]

        mp = defaultdict(str)
        visited = set()

        def dfs(node):
            visited.add(node)
            parent_color = mp[node]
            for neigh in adj[node]:
                if neigh in visited:
                    if mp[neigh] == parent_color:
                        return False
                    continue

                if parent_color == "G":
                    mp[neigh] = "Y"

                if parent_color == "Y":
                    mp[neigh] = "G"

                if not dfs(neigh):
                    return False
            return True

        for node in range(len(graph)):
            if node in visited:
                continue
            mp[node] = "G"
            if not dfs(node):
                return False

        return True