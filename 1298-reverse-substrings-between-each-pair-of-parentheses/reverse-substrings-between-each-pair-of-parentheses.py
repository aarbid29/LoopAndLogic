class Solution:
    def reverseParentheses(self, s: str) -> str:


        res = ""
        numstack = []
        bracstack = []
        stack =[]



        for i , char in enumerate(s):
            if char == ')':
                build = []
                while stack and stack[-1]!= "(":
                    build.append(stack.pop())

                stack.pop()
                stack.extend(build)
            else:
                stack.append(char)

        return "".join(stack)













