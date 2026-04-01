class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        newIntervals = intervals[0]

        res = []
        res.append(newIntervals)
        for interval in intervals:
            if newIntervals[1] >= interval[0]:
                newIntervals[1] = max(interval[1], newIntervals[1])
            else:
                newIntervals = interval
                res.append(newIntervals)
        
        return res

        