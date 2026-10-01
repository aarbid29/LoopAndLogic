class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack  = []
        count = 0
        remove = set() 
        build = ""

        for  i , char in enumerate(s):

            if char == "(":
                stack.append(i)
            elif char==")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
            else:
                continue
        
        for j in stack:
            remove.add(j)

        for i,char in enumerate(s):
            if i not in remove:
                build+= char
        return build
        














        



        