class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x:x[1])
        visited_end = intervals[0][1]
        visited_start = intervals[0][0]
        count = 0

        for start,end in intervals[1:]:
            if start<visited_end:
                count+=1
            else:
                visited_end = end

        return count

        



        