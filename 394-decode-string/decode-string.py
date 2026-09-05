class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        numbers = []
        res = ""
        num = 0
        for i in range(len(s)):
            val = s[i]
            if val == "[" or val =="]" or  val.isalpha():
                if num is not None:
                    numbers.append(num)
                    num = None
                #main code here
                if val =="]":
                    res = ""
                    while stack and stack[-1]!= "[":
                        res =  stack.pop() + res
                    multiply = numbers.pop() if numbers else 1 
                    res = res * multiply
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(val)
            else:
                num= num*10 + int(val) if num is not None else int(val)
        return "".join(stack)





        
        