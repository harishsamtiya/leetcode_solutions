class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            stack = [(i, j)]
            grid[i][j] = -1
            while stack:
                i, j = stack.pop()

                if i+1 < n and grid[i+1][j] == 1:
                    grid[i+1][j] = -1
                    stack.append((i+1, j))

                if 0 <= i-1 and grid[i-1][j] == 1:
                    grid[i-1][j] = -1
                    stack.append((i-1, j))

                if j+1 < m and grid[i][j+1] == 1:
                    grid[i][j+1] = -1
                    stack.append((i, j+1))

                if 0 <= j-1 and grid[i][j-1] == 1:
                    grid[i][j-1] = -1
                    stack.append((i, j-1))

        def isConnected():
            islandCount = 0
            connected = True
            allZeros = True
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        allZeros = False
                        if islandCount == 1:
                            connected = False
                            break
                        islandCount += 1
                        dfs(i, j)
                if connected == False:
                    break
            
            if allZeros:
                return False

            for i in range(n):
                for j in range(m):
                    if grid[i][j] == -1:
                        grid[i][j] = 1
            
            return connected
        
        if not isConnected():
            return 0

        result = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not isConnected():
                        return 1
                    grid[i][j] = 1
        return 2
