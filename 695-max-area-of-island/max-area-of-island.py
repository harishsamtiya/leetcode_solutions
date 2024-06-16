class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 2
                return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
            return 0
        
        maximum_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maximum_area = max(maximum_area, dfs(i, j))
        
        return maximum_area