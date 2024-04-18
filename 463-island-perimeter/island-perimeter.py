class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        queue = deque()

        for i in range(n):
            flag = False
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    flag = True
                    break
            if flag:
                break
            
        
        perimeter = 0
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            i, j = queue.popleft()
            grid[i][j] = -1
            for x, y in moves:
                if 0 <= i+x < n and 0 <= j+y < m and grid[i+x][j+y] != 0:
                    if grid[i+x][j+y] == 1:
                        queue.append((i+x, j+y))
                        grid[i+x][j+y] = -1
                else:
                    perimeter += 1
                
            

        return perimeter


        
