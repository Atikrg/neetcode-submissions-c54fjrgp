class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])    
        n = len(intervals)
        newInterval = intervals[0]
        res = []
        res.append(newInterval)
        for interval in intervals:
            if interval[0] <= newInterval[1]:
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                newInterval = interval
                res.append(newInterval)

        return res