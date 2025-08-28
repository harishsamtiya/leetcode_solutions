class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for col in range(n-2, 0, -1):
            li = []
            for r in range(n - col):
                li.append(grid[r][col+r])
            li.sort()

            for r in range(n - col):
                grid[r][col+r] = li[r]

    
        for row in range(n-1):
            li = []
            for c in range(n-row):
                li.append(grid[row+c][c])
            
            li.sort(reverse=True)
            for c in range(n-row):
                grid[row+c][c] = li[c]

        return grid

