/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
    /**
     * @param {Interval[]} intervals
     * @returns {boolean}
     */
    canAttendMeetings(intervals) {
        intervals.sort((a, b) => a.start - b.start);

    // Iterate through intervals, checking for overlaps
    for (let i = 1; i < intervals.length; i++) {
        let current = intervals[i];
        let previous = intervals[i - 1];

        // If the current interval starts before the previous one ends, there's an overlap
        if (current.start < previous.end) {
            return false;
        }
    }

    return true;
    }
}