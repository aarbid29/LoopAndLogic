class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        state = [0] * len(graph)

        def dfs(node):
            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            state[node] = 1

            for neigh in graph[node]:
                if not dfs(neigh):
                    return False

            state[node] = 2
            return True

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res