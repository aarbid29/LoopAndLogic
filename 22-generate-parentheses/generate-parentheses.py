class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        res = []
        def dfs(openn,close,sol):
            
            if close == n and openn == n:
                st = "".join(sol)
                res.append(st)
                return 
            if close >n:
                return
            if openn>n:
                return
            
            if openn>=close:
                sol.append("(")
                dfs(openn+1,close,sol)
                sol.pop()

            if close<= openn:
                sol.append(")")
                dfs(openn,close+1,sol)
                sol.pop()

        
        dfs(0,0,[])
        return res
            
        




        