# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# Time: O(nlogn)
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # O(nlogn)
        intervals = sorted(intervals, key=lambda val: val.start)

        idx = 0
        while(len(intervals) > idx+1): # O(n)
            if intervals[idx].end >= intervals[idx+1].start:
                intervals[idx].end = max(intervals[idx].end, intervals[idx+1].end)
                del intervals[idx+1]
            else: 
                idx += 1
        return intervals

# Test
ans = Solution().merge([Interval(1, 3), Interval(2, 5), Interval(10, 12), Interval(3, 5)])
for val in ans:
    print(val.start, val.end)

