class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        class DSU:
            def __init__(self):
                self.parent = {}
                self.rank = {}
                self.size = {}
            def find(self, x):
                if x not in self.parent:
                    self.parent[x] = x
                    self.rank[x] = 1
                    self.size[x] = 1
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
                    self.size[px] += self.size[py]
                elif self.rank[py] > self.rank[px]:
                    self.parent[px] = py
                    self.size[py] += self.size[px]
                else:
                    self.parent[py] = px
                    self.rank[px] += 1
                    self.size[px] += self.size[py]
                return True

        x_mp = defaultdict(list)
        y_mp = defaultdict(list)
        dsu = DSU()
        row = len(grid)
        col = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    x_mp[r].append((r,c))
                    y_mp[c].append((r,c))
        #connecting all serves at same column
        for c,value in y_mp.items():
            if len(value)==1:
                continue
            fx,fy = value[0]
            for x,y in value[1:]:
                dsu.union((fx,fy),(x,y))

        #connecting all servers in same row
        for r, value in x_mp.items():
            if len(value)==1:
                continue
            fx,fy = value[0]
            for x,y in value[1:]:
                dsu.union((fx,fy),(x,y))
                    
                    
        ans = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    root = dsu.find((r, c))

                    if dsu.size[root] > 1:
                        ans += 1

        return ans
                    
        

        

                    


        