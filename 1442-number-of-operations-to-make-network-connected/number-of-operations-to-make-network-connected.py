class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1:
            return -1
        #adj list crecate
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [1] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                px = self.find(x)
                py = self.find(y)

                if px == py:
                    return False

                if self.rank[px] > self.rank[py]:
                    self.parent[py] = px
                elif self.rank[py] > self.rank[px]:
                    self.parent[px] = py
                else:
                    self.parent[py] = px
                    self.rank[px] += 1

                return True

        dsu = DSU(n)
        count =0 

        for c1,c2 in connections:
            if dsu.union(c1,c2):
                continue
            else:
                count+=1

        
        parents = set()

        for i in range(n):
            parents.add(dsu.find(i))

        components = len(parents)

        if count>= components-1:
            return components-1
        else:
            return -1

            
                          

        

    








        