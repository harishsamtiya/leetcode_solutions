class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n < 2:
            return grid[0][0]

        def twoMinIds(row):
            minId, secId = 0, 1
            if grid[row][0] > grid[row][1]:
                minId, secId = 1, 0
            
            for i in range(2, n):
                tempi = i

                if grid[row][minId] > grid[row][i]:
                    tempi = minId
                    minId = i
                
                if grid[row][secId] > grid[row][tempi]:
                    secId = tempi
            
            return (minId, secId)
        
        minId, secId = twoMinIds(0)

        for i in range(1, n):
            grid[i][minId] += grid[i-1][secId] - grid[i-1][minId]
            minValue = grid[i-1][minId]
            minId, secId = twoMinIds(i)
            grid[i][minId] += minValue
            grid[i][secId] += minValue
        return grid[n-1][minId]
        

