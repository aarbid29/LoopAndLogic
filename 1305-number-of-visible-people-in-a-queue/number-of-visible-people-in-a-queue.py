class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:

        ngecount = [0]*len(heights)
        stack = []

        for i in range(len(heights) - 1, -1, -1):
            num = heights[i]


            while stack and heights[stack[-1]] < num:
                before = stack.pop()
                ngecount[i]+=1

            if stack :
                ngecount[i] += 1
            stack.append(i)

        return ngecount 

