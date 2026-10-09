class Solution:
    def minimumDeletions(self, s: str) -> int:

        n = len(s)
        stack =[]

        stack = []
        remove = 0
        flip = 0

        # for i,char in enumerate(s):

        #     if char == "a":
        #         if stack and stack[-1]=="b":
        #             #have two option , remove b or add curr a 
                    

        #         else:
        #             stack.append(char)

        #     else:
        #         stack.append(char)
        # return remove
        count = 0
        for char in reversed(s):
            if char == "b" and stack and stack[-1] == "a":
                stack.pop()
                count += 1
            else:
                stack.append(char)

        return count


