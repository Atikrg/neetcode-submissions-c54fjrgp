/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
 // Sort intervals by start time using a lambda expression
    intervals.sort(Comparator.comparingInt(interval -> interval.start));

    // Iterate through intervals, checking for overlaps
    for (int i = 1; i < intervals.size(); i++) {
      Interval current = intervals.get(i);
      Interval previous = intervals.get(i - 1);

      // If the current interval starts before the previous one ends, there's an overlap
      if (current.start < previous.end) {
        return false;
      }
    }

    return true;
    }
}
