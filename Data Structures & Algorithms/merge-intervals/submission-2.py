class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])

        res = []

        n = len(intervals)

        newInterval = intervals[0]

        res.append(newInterval)


        i = 0; 

        for interval in intervals:

            if(interval[0] <= newInterval[1]):
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                newInterval = interval
                res.append(newInterval)

            i+=1

        return res