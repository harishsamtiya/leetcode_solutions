class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        flow_ocean = [[True]*m for _ in range(n)]
        cols = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            flow_ocean[i][j] = False
            pacific, atlantic = False, False
            for r, c in cols:
                row = i + r
                col = j + c
                if pacific and atlantic:
                    break
                elif ((row == 0 and col == m-1) or (col == 0 and row == n-1)) and heights[i][j] >= heights[row][col]:
                    pacific = True
                    atlantic =  True
                elif row < 0 or col < 0:
                    pacific = True
                elif row >= n or col >= m:
                    atlantic =  True
                elif flow_ocean[row][col] and heights[i][j] >= heights[row][col]:
                    pac, atlan = dfs(row, col)
                    pacific = pacific or pac
                    atlantic = atlantic or atlan
                    
            flow_ocean[i][j] = True
            return (pacific, atlantic)

        result = []
        for i in range(n):
            for j in range(m):
                pac, atlan = dfs(i, j)
                if pac and atlan:
                    result.append([i, j])
        return result
                    