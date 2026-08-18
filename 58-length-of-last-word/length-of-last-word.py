class Solution:
    def lengthOfLastWord(self, s: str) -> int:


        s = s[::-1].lstrip(" ")
        cnt = 0

        for i in s:
            if i == " ":
                break

            cnt+=1
        return cnt






        