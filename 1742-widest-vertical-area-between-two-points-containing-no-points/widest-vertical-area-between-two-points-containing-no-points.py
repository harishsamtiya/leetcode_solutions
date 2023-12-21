class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        area = 0
        points.sort()
        n = len(points)

        for i in range(n-1):
            area = max(area, points[i+1][0] - points[i][0])

        return area

