

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        if not intervals:
            return 0

        n = len(intervals)
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]

        start.sort()
        end.sort()

        res = 0
        count = 0
        s = 0
        e = 0

        while s < n:
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)

        return res
