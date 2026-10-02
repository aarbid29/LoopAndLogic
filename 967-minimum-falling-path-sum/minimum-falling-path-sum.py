class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        directions = [(1,-1),(1,0),(1,1)]
        maxx = float("inf")
        res = float("inf")
        visited =set()
        

        @lru_cache(None)
        def dfs(r,c):
            if r==row-1:
                return 0

            maxx = float("inf")
            for dr,dc in directions:
                nr,nc = dr+r ,dc+c

                if not(0<=nr<row and 0<=nc<col):
                    continue
                
                tmp = matrix[nr][nc] +dfs(nr,nc)
                maxx = min(maxx,tmp)
            
            return maxx
        

        for c in range(col):
            res = min(res,matrix[0][c]+dfs(0,c))
        
        return res








        