class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        stack.append(0)


        for i in range(1,len(temperatures)):
            curr = temperatures[i]

            while stack and temperatures[stack[-1]]<curr:
                indi = stack.pop()
                res[indi] = i-indi

            stack.append(i)

   
        return res
        