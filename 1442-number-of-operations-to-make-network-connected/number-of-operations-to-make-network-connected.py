class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        class DSU:
            def __init__(self,n):
                self.parent = list(range(n))
                self.rank = [1]*n

            def find(self,x):
                if self.parent[x]!=x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x,y):
                px = self.find(x)
                py = self. find(y)

                if px == py:
                    return False
                if self.rank[px]>self.rank[py]:
                    self.parent[py] = px
                elif self.rank[py]>self.rank[px]:
                    self.parent[px] = py
                else:
                    self.parent[py] = px
                    self.rank[px]+=1
                return True

        dsu = DSU(n)
        visited = set()
        used = 0 
        extra = 0

        for u ,v in connections:
            if dsu.union(u,v):
                used+=1
            else:
                extra +=1
        needed = 0

        needed = n-used-1
        if extra >=needed:
            return needed
        else:
            return -1
            


        






