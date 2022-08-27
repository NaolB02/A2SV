class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals = sorted(intervals)
        while i + 1 < len(intervals):
            if intervals[i][1] >= intervals[i + 1][0]:
                end = max(intervals[i][1], intervals[i + 1][1])
                intervals[i] = [intervals[i][0], end]
                intervals.pop(i + 1)

            else:
                i += 1
        
        return intervals
