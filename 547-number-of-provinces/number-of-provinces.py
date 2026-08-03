class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    adj[i].append(j)
        
        visited = set()
        count = 0

        def dfs(node):

            if node in visited:
                return
            visited.add(node)
            for neigh in adj[node]:
                dfs(neigh)
            return
        for node in range(len(isConnected)):
            if node not in visited:
                count += 1
                dfs(node)
        return count

            


