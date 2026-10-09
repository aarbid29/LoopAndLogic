class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for s , d , w in edges:
            adj[s].append((d,w))
            adj[d].append((s,2*w))
        visited =set()
        dp = [float("inf")]*n

        heap  = []

        heapq.heappush(heap,(0,0))
        while heap:
            cost , node = heapq.heappop(heap)
            if cost > dp[node]:
                continue

            for neigh ,weight in adj[node]:

                newweight = cost+weight

                if newweight < dp[neigh]:
                    dp[neigh]=newweight
                    heapq.heappush(heap,(newweight,neigh))
        
        if dp[n-1]==float("inf"):
            return -1
        else:
            return dp[n-1]





        
        