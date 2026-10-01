class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        openn = 0
        extraneeded = 0


        i = 0 
        n = len(s)

        while i < n:

            if s[i]=="(":
                openn+=1
                i+=1
            else:

                if i+1 < n and s[i] == s[i+1]:
                    i+=2

                
                else:
                    extraneeded +=1
                    i+=1

                if openn>0:
                    openn-=1
                else:
                    extraneeded+=1
        
        extraneeded += openn*2

        return extraneeded



                        



