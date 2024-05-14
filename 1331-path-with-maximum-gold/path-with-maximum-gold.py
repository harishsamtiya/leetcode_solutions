class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            if i <  0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return 0
            
            val = grid[i][j]
            grid[i][j] = 0

            gold = max(dfs(i+1, j), dfs(i-1, j), dfs(i, j+1) , dfs(i, j-1)) + val
            grid[i][j] = val
            return gold
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans