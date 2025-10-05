class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        oceans = [[[False]*m for _ in range(n)], [[False]*m for _ in range(n)]]
        cols = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = []
        stack = []

        for j in range(m):
            oceans[0][0][j] = True
            oceans[1][n-1][j] = True
            stack.append((0, 0, j))
            stack.append((1, n-1, j))
        for i in range(n):
            oceans[0][i][0] = True
            oceans[1][i][m-1] = True
            stack.append((0, i, 0))
            stack.append((1, i, m-1))

        while stack:
            curr_ocean, i, j = stack.pop()

            for r, c in cols:
                row, col = i + r, j + c
                if 0 <= row < n and 0 <= col < m and (not oceans[curr_ocean][row][col]) and heights[i][j] <= heights[row][col]:
                    oceans[curr_ocean][row][col] = True
                    stack.append((curr_ocean, row, col))
        

        for row in range(n):
            for col in range(m):
                if oceans[0][row][col] and oceans[1][row][col]:
                    result.append([row, col])
        return result

        
        