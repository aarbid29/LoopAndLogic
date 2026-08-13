class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(i,sol,total):
            if total==n:
                if len(sol)==k:
                    res.append(sol[:])

                return
            if total>n:
                return 
            
            for i in range(i,10):
                sol.append(i)
                backtrack(i+1,sol,total+i)
                sol.pop()

        backtrack(1,[],0)
        return res






        