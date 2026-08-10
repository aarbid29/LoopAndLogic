class Solution:
    def compress(self, chars: List[str]) -> int:
        res =""
        prev = ""
        prev = chars[0]
        count=1

        for char in chars[1:]:
            if char == prev:
                count += 1
            else:
                res += prev
                if count > 1:
                    res += str(count)
                prev = char
                count = 1

        res += prev
        if count > 1:
            res += str(count)

        for i in range(len(res)):
            chars[i] = res[i]

        return len(res)
            


        