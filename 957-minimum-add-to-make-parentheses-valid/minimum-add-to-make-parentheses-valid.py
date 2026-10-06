class Solution:
    def minAddToMakeValid(self, s: str) -> int:


        extraneeded = 0
        stack = []


        for char in s:

            if char == "(":
                stack.append(char)            
            else:
                if stack:
                    
                    stack.pop()
                else:
                    extraneeded+=1
        return len(stack) + extraneeded