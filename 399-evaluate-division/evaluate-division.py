class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        res = []

        adj = defaultdict(list)
        visited= set()

        for i ,(src,dst) in enumerate(equations):
            adj[src].append((dst,values[i]))
            adj[dst].append((src,1/values[i]))
        
        def dfs(node,dst):

            visited.add(node)
            for neigh,value in adj[node]:
                if neigh in visited:
                    continue

                if neigh ==dst:
                    ans = value
                    return ans
                

                ans = dfs(neigh,dst)
                if ans!= -1:
                    return ans*value
            
            return -1

        for src,dst in queries:

            if src not in adj or dst not in adj:
                res.append(float(-1))
                continue
            if src == dst:
                res.append((float(1)))
                continue
            visited.clear()
            res.append(dfs(src,dst))
        
        return res
            


            
        
        