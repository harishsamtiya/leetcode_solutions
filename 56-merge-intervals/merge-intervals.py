class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        def overlap(interval1, interval2):
            s1, e1 = interval1
            s2, e2 = interval2

            if s1 <= s2 <= e1:
                return True
            return False

        result = []
        result.append(intervals[0])
        for i in range(1, n):

            if overlap(result[-1], intervals[i]):
                s1, e1 = result.pop()
                s2, e2 = intervals[i]
                result.append((s1, max(e1, e2)))
            else:
                result.append(intervals[i])
        return result