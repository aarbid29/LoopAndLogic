class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for req , pre in prerequisites:
            adj[pre].append(req)
        
        visited = set()
        globall = set()
        order = []


        def dfs(node):
            nonlocal order
            if node in visited:
                return False
            if node in globall :
                return False
            visited.add(node)
            for neigh in adj[node]:
                if neigh in globall:
                    continue
                if not dfs(neigh):
                    visited.remove(node)
                    return False

            globall.add(node)
            visited.remove(node)
            order.append(node)
            return True
        
        for i in range(numCourses):
            if i not in globall:
                if not dfs(i):
                    return []
        return order[::-1]
                

        







         

        




        