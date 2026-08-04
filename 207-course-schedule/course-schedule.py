from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for take, pre in prerequisites:
            adj[pre].append(take)

        visited = set()
        curr = set()
        boool = True

        def dfs(n):
            nonlocal boool

            if n in curr:
                boool = False
                return

            if n in visited or not boool:
                return

            visited.add(n)
            curr.add(n)

            for neigh in adj[n]:
                dfs(neigh)

            curr.remove(n)

        for i in range(numCourses):
            if i not in visited:
                dfs(i)

            if not boool:
                return False

        return boool
