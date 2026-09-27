class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []
        newbeg = intervals[0][0]
        newend = intervals[0][1]
        add = True

        a = newInterval[0]
        b = newInterval[1]
        if b< newbeg:
            newbeg  = a
            newend = b
            add = False
        for start, end in intervals:
            if add:
                if a > newend and b < start:
                    res.append([newbeg, newend])
                    res.append([a, b])
                    newbeg = start
                    newend = end
                    add = False
                    continue

                if start > newend:
                    res.append([newbeg, newend])
                    newbeg = start
                    newend = end
                if a <= newend:
                    newbeg = min(newbeg, a)
                    newend = max(newend, b)
                    add = False



                if start <= newend:
                    newbeg = min(newbeg, start)
                    newend = max(newend, end)
                    continue

            else:
                if start > newend:          
                    res.append([newbeg, newend])
                    newbeg = start
                    newend = end
                    continue
                else:
                    newbeg = min(newbeg, start)
                    newend = max(newend, end)

        res.append([newbeg, newend])

        if add:
            res.append([a, b])

        return res