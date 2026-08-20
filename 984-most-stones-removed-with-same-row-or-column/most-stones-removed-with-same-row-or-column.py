class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        class DSU:
            def __init__(self):
                self.parent = {}
                self.rank = {}

            def find(self, x):
                if x not in self.parent:
                    self.parent[x] = x
                    self.rank[x] = 1

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

        dsu = DSU()
        connected = 0
        x_mp = defaultdict(list)
        y_mp = defaultdict(list)
        for x,y in stones:
            x_mp[x].append((x,y))
            y_mp[y].append((x,y))

        for stones_in_row in x_mp.values():
            first = stones_in_row[0]

            for stone in stones_in_row[1:]:
                if dsu.union(first, stone):
                    connected += 1

        for stones_in_col in y_mp.values():
            first = stones_in_col[0]

            for stone in stones_in_col[1:]:
                if dsu.union(first, stone):
                    connected += 1

        n = len(stones)
        return  connected
