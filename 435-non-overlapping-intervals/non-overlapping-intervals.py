class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()

        count = 0
        end = -50000

        for s, e in intervals:
            if s < end:
                count += 1
                end = min(end, e)
            else:
                end = e
            
        
        return count

        