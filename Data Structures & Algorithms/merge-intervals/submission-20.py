class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        result = []    
        intervals.sort(key = lambda x: x[0])


        newInterval = intervals[0]

        j = 0

        result.append(newInterval)
        for i in range(1, len(intervals)):

            if newInterval[1] >= intervals[i][0]:
                newInterval[1] = max(newInterval[1], intervals[i][1])
            
            else:
                newInterval = intervals[i]
                result.append(newInterval)


        return result