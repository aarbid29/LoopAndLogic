class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        strr = "".join(map(str, digits))
        intt = int(strr) + 1
        str1 = str(intt)

        return list(map(int, str1))