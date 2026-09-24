class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        row = len(mat)
        col = len(mat[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        l = 0
        r = col-1

        while l <=r :
            mid = (l+r)//2
            max_row = 0
            for i in range(row):
                if mat[i][mid]> mat[max_row][mid]:
                    max_row = i
            
            left = mat[max_row][mid - 1] if mid>0 else -1
            right = mat[max_row][mid + 1] if mid<col-1 else -1
            curr = mat[max_row][mid]

            if curr >left and curr>right:
                return [max_row,mid]
            elif left > curr:
                r= mid-1
            else:
                l = mid+1
        return [-1,-1] 
            



            
            

            


            


