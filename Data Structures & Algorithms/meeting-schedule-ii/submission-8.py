"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0;
        
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]

        start.sort()
        end.sort()

        res = 0
        count = 0
        s = 0
        e = 0

        n = len(intervals)

        while s < n:
            if start[s] < end[e]:
                count+=1
                s+=1

            else:
                count -= 1
                e+=1
            res = max(res, count)

        return res

