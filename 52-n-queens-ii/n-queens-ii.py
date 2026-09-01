class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        
        matrix = [["."]*n for _ in range(n)]
        res = 0
        col_visited= set()
        diag1_visited = set() #for /
        diag2_visited= set() # for \


        def backtrack(r):
            nonlocal res


            for col in range(n):
                r,c = r,col

                if c in col_visited:
                    continue
                #diag check:
                if (r-c) in diag2_visited:
                    continue
                if(r+c) in diag1_visited:
                    continue
            
                matrix[r][c]= 'Q'
                col_visited.add(c)

                diag1_visited.add(r+c)
                diag2_visited.add(r-c)

                if r == n - 1:
                    res+=1
                else:
                    backtrack(r + 1)


                diag1_visited.remove(r+c)
                diag2_visited.remove(r-c)
                col_visited.remove(c)
                matrix[r][c]= "."
        
        backtrack(0)
        return res
            
            









            


