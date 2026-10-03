class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        maxseen = []
        count = 0 
        maxx =nums[0]
        stack = []
        stack.append((nums[0],0))
        for i, num in enumerate(nums[1:], start=1):
            # nums[1:] creates a sliced array whose indexing starts at 0.
            if num < stack[-1][0]:
                count+=1
                if count ==2 :
                    return False

                if stack[-1][1]!=0:
                    before,indi = stack[-2]

                    if before > num:
                        stack.append((stack[-1][0],i))
                    else:
                        stack.append((num,i))  
                else:
                    stack.pop()
                    stack.append((num,i))
            else:
                stack.append((num,i))

        return True



        