class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[0])

        count = 0
        prev = intervals[0]

        for i in range(1, len(intervals)):

            if intervals[i][0] < prev[1]:
                # Overlap → remove one interval
                count += 1

                # Keep the interval that ends earlier
                if intervals[i][1] < prev[1]:
                    prev = intervals[i]

            else:
                prev = intervals[i]

        return count