class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        dq = deque()
        visited= set()
        row = len(mat)
        col = len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    dq.append((i,j,0))
                    visited.add((i,j))
        while dq:
            size = len(dq)
            for i in range(size):
                r,c,dist = dq.popleft()

                for dr,dc in directions:
                    nr,nc = dr+r ,dc+c

                    if 0 <= nr < row and 0 <= nc < col:
                        if (nr,nc) in visited:
                            continue
                        if mat[nr][nc]==1:
                            mat[nr][nc] = dist+1
                            dq.append((nr,nc,dist+1))
                            visited.add((nr,nc))
        return mat







        