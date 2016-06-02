class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "(" + str(self.start) + ", " + str(self.end) + ")"

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) > 0:
            intervals.sort(key=lambda x : x.start)
            prev = intervals[0]
            merged_list = []
            for index in range(1, len(intervals)):
                if (intervals[index].start >= prev.start and intervals[index].start <= prev.end):
                    prev.start = min(prev.start, intervals[index].start)
                    prev.end = max(prev.end, intervals[index].end)
                else:
                    merged_list.append(prev)
                    prev = intervals[index]
            merged_list.append(prev)
            return merged_list
        else:
            return intervals

intervals = [
    Interval(1,10),
    Interval(2,9),
    Interval(3,8),
    Interval(4,7),
    Interval(5,6),
    Interval(6,6)
    ]

sol = Solution()
for interval in sol.merge(intervals):
    print interval,
