class Solution:
    def minSwaps(self, s: str) -> int:


        stack = []
        close = 0
        maxclose = 0
        for i ,brack in enumerate(s):

            if brack =="[":
                close-=1
            else:
                close+=1
                maxclose = max(maxclose,close)

        return math.ceil(maxclose/2)

        








        