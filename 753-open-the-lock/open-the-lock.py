from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dq = deque([("0000", 0)])
        deadend = set(deadends)
        visited = {"0000"}

        if "0000" in deadend:
            return -1

        while dq:
            combinations, tries = dq.popleft()

            if combinations == target:
                return tries

            for i in range(4):

                if combinations[i] == "9":
                    new_comb1 = combinations[:i] + "0" + combinations[i+1:]
                else:
                    new_comb1 = combinations[:i] + str(int(combinations[i]) + 1) + combinations[i+1:]

                if combinations[i] == "0":
                    new_comb2 = combinations[:i] + "9" + combinations[i+1:]
                else:
                    new_comb2 = combinations[:i] + str(int(combinations[i]) - 1) + combinations[i+1:]

                if new_comb1 not in visited and new_comb1 not in deadend:
                    visited.add(new_comb1)
                    dq.append((new_comb1, tries + 1))

                if new_comb2 not in visited and new_comb2 not in deadend:
                    visited.add(new_comb2)
                    dq.append((new_comb2, tries + 1))

        return -1