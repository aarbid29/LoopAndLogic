class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # brackets = s.split()
        sett =set()
        stack = []

        for i  in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                beg = stack.pop()
                if not stack:
                    sett.add(beg)
                    sett.add(i)

        strr = ""
        for i,brac in enumerate(s):
            if i in sett:
                continue
            strr+=brac
        return strr

        
        

            
        

             