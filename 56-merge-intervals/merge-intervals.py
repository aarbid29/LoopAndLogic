class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_beg = intervals[0][0]
        new_end = intervals[0][1]
        res = []
        for start, end in intervals[1:]:
            if start > new_end:
                res.append([new_beg, new_end])
                new_beg = start
                new_end = end
            elif end > new_end:
                new_end = end

        res.append([new_beg, new_end])
        return res
        