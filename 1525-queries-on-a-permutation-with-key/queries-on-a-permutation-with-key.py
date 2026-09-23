class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        perm = list(range(1, m + 1))

        res = []


        for query in queries:

            idx  = perm.index(query)
            res.append(idx)

            perm.pop(idx)
            perm.insert(0,query)

        return res
        