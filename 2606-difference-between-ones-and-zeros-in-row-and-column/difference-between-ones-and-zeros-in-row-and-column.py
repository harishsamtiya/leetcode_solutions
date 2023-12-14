class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        rows = [0]*n
        cols = [0]*m

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        
        for i in range(n):
            for j in range(m):
                grid[i][j] = 2*(rows[i] + cols[j]) - n - m
        
        return grid