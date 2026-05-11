"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        


        start = [x.start for x in intervals]
        end = [y.end for y in intervals]

        start.sort()
        end.sort()

        n = len(intervals)

        s = 0
        e = 0
        
        count = 0
        res = 0
        while s < n:
            if start[s] < end[e]:
                count += 1
                s += 1

            else:
                count -= 1
                e += 1

            res = max(res, count)

        return res