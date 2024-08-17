class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n , m = len(points), len(points[0])
        result = points[0]

        for i in range(1, n):

            for j in range(1, m):
                result[j] = max(result[j-1]-1, result[j])
            
            for j in range(m-2, -1, -1):
                result[j] = max(result[j+1]-1, result[j])
            
            for j in range(m):
                result[j] = points[i][j] + result[j]


        return max(result) 