class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        def overlap(interval1, interval2):
            s1, e1 = interval1
            s2, e2 = interval2

            if s1 <= s2 <= e1 or s2 <= s1 <= e2 or s1 <= e2 <= e1 or s2 <= e1 <= e2:
                return True
            return False

        

        result = []
        flag = True
        for i in range(n):
            start, end = intervals[i]

            if overlap(intervals[i], newInterval):
                newInterval = (min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1]))
            else:
                if flag and intervals[i][0] > newInterval[0]:
                    result.append(newInterval)
                    flag = False
                result.append(intervals[i])
        
        if flag:
            result.append(newInterval)
        return result

