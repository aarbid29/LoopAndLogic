class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        used= set()
        seen = set()
        n = len(digits)
        count = 0

        def backtrack(sol):
            nonlocal count
            if len(sol)==3:
                number = int("".join(map(str, sol)))
                if number%2==0 and number not in seen:
                    seen.add(number)
                    count+=1
                return

            for i in range(len(digits)):
                if i in used:
                    continue
                if len(sol) == 0 and digits[i] == 0:
                    continue
                used.add(i)
                sol.append(digits[i])
                backtrack(sol)
                sol.pop()
                used.remove(i)

            return
        backtrack([])
        return count

        backtrack([])



