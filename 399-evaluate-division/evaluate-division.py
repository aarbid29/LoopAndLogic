class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i , (source,dist) in enumerate(equations):
            div = values[i]
            adj[source].append((dist,div))
            adj[dist].append((source,1/div))
        
        res = []
        visited = set()
        def dfs(node ,dst ,mul):
            if node == dst:
                return mul

            visited.add(node)
            for neigh,weight in adj[node]:
                if neigh in visited:
                    continue
                result = dfs(neigh , dst , mul* weight)

                if result!=-1:
                    return result
            
            return -1

        for src , dst in queries:
            if src not in adj or dst not in adj:
                res.append(-1.0)
                continue
            visited.clear()
            res.append(dfs(src,dst,1))
        return res
                
                
                



        
        



        