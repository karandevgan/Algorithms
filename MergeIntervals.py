# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

     def __str__(self):
         return "(" + str(self.start) + ", " + str(self.end) + ")"


class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval

    def insert(self, intervals, new_interval):
        if (new_interval.start > new_interval.end):
            new_interval.start, new_interval.end = new_interval.end, new_interval.start

        non_merged_intervals = []


        min_interval = float('inf')
        max_interval = 0
        isIntervalsModified = False
        loop_run = 0
        original_length = len(intervals)
        if original_length > 0:
            i = 0
            while True:
                if self.isOverlap(intervals[i], new_interval):
                    isIntervalsModified = True
                    intervals[i] = Interval(min(intervals[i].start, new_interval.start),
                                             max(intervals[i].end, new_interval.end))
                    min_interval = min(min_interval, intervals[i].start)
                    max_interval = max(max_interval, intervals[i].end)
                else:
                    non_merged_intervals.append(intervals[i])
                i += 1
                if (i == original_length):
                    break

        if len(intervals) > 0:
            if isIntervalsModified:
                non_merged_intervals.append(Interval(min_interval, max_interval))
            else:
                non_merged_intervals.append(new_interval)
        else:
            non_merged_intervals = [new_interval]

        non_merged_intervals.sort(key=lambda x: x.start)

        return non_merged_intervals

    def isOverlap(self, interval, new_interval):
        isOverlapping = False
        if (new_interval.start >= interval.start and new_interval.start <= interval.end) or \
            (new_interval.end >= interval.start and new_interval.end <= interval.end) or \
            (interval.start > new_interval.start and interval.start <= new_interval.end) or \
                (interval.end > new_interval.start and interval.end <= new_interval.end):
            isOverlapping = True
        return isOverlapping

i1 = Interval(1,3)
i2 = Interval(6,9)
intervals = [Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(12,16)]
new_interval = Interval(4,9)

sol = Solution()
for interval in sol.insert(intervals, new_interval):
    print interval
