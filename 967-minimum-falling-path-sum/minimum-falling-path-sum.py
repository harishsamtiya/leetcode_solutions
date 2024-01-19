class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(1, n):
            for j in range(m):
                dleft = float('inf') if j-1<0 else matrix[i-1][j-1]
                dcenter = matrix[i-1][j]
                dright = float('inf') if j+1>=m else matrix[i-1][j+1]

                matrix[i][j] += min(dleft, dright, dcenter)
        
        return min(matrix[n-1])
