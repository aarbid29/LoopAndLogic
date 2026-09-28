class Solution:
    def maxDepth(self, s: str) -> int:


        stack = []
        maxx = 0
        openn = 0
        for i,s in enumerate(s):
            if s=="(":
                openn+=1
                maxx = max(maxx,openn)
            elif s ==")":
                openn-=1
            else:
                maxx = max(maxx,openn)
        
        return maxx
                

        