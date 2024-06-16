class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()

        m = len(grid)
        n = len(grid[0])
        freshCount = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    freshCount += 1
        
        queue.append((-1, -1))
        count = 0

        while queue:
            i, j = queue.popleft()
            if i == -1:
                if queue:
                    count += 1
                    queue.append((-1, -1))
            else:
                if 0 <= i+1 < m and 0 <= j < n and  grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    freshCount -= 1
                    queue.append((i+1, j))
                if 0 <= i-1 < m and 0 <= j < n and  grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    freshCount -= 1
                    queue.append((i-1, j))
                if 0 <= i < m and 0 <= j+1 < n and  grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    freshCount -= 1
                    queue.append((i, j+1))
                if 0 <= i < m and 0 <= j-1 < n and  grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    freshCount -= 1
                    queue.append((i, j-1))
        

        return count if freshCount == 0 else -1