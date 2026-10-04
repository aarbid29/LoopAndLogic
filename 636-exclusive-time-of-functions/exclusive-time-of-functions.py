class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:

        result= [0]* (n)

        stack = []
        # "0:start:0"
        # [0 , start , 0]
        log = []
        prevtime = 0
        for log in logs:

            funct , operation , timee = log.split(":")
            func = int(funct)
            time = int(timee)

            if operation == "start":

                if stack :
                    result[stack[-1][0]]+= (time - prevtime)
                stack.append((func , operation , time ))
                prevtime = time
            else:
                result[stack[-1][0]] += time - prevtime + 1
                stack.pop()
                prevtime=time+1
        return result







        