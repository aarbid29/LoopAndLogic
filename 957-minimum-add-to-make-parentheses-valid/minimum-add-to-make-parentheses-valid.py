class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        needed = set()
        count = 0

        for i,char in enumerate(s):

            if char == "(":
                stack.append(char)
            else :
                if stack:
                    stack.pop()
                else:
                    count+=1
            
        n =len(stack)
        count+=n
        return count
        