class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        stack = []
        flip = 0

        for num in s:


            if num == "0" and stack and stack[-1]=="1":
                flip+=1
                stack.pop()
            else:
                stack.append(num)
        return flip
        