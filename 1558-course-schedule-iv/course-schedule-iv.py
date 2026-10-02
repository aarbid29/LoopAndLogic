class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for pre , req in prerequisites:
            adj[pre].append(req)
        visited = set()
        def dfs(node , dst):
            if node in visited:
                return False
            
            visited.add(node)

            for neigh in adj[node]:

                if neigh == dst:
                    return True
                
                if dfs(neigh,dst):
                    return True
            
            return False
        
        res = []
        for source ,dst in queries:
            visited.clear()
            res.append(dfs(source,dst))

        return res




        