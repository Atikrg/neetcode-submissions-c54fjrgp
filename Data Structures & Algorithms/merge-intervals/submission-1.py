class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        # Sort intervals based on the starting value
        intervals.sort(key=lambda x: x[0])

        result = []
        new_interval = intervals[0]
        result.append(new_interval)

        for interval in intervals:
            if interval[0] <= new_interval[1]:  # Overlapping intervals
                new_interval[1] = max(new_interval[1], interval[1])
            else:
                new_interval = interval
                result.append(new_interval)

        return result
