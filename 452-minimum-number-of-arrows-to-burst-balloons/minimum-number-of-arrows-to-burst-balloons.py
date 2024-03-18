class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()
        ans = 1
        pEnd = points[0][1]
        for i in range(1, n):
            cStart, cEnd = points[i]

            if cStart <= pEnd:
                pEnd = min(pEnd, cEnd)
            else:
                pEnd = cEnd
                ans += 1
        return ans