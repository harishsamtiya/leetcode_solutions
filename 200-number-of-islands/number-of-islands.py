class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def bfs(i, j):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == "1":
                grid[i][j] = "2"

                bfs(i+1, j)
                bfs(i-1, j)
                bfs(i, j+1)
                bfs(i, j-1)
        
        no_of_islands = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    no_of_islands += 1
                    bfs(i, j)
        return no_of_islands