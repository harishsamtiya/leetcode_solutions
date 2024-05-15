class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        theifs = deque()
        distances = [[0]*n for _ in range(n)]
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    theifs.append((i, j, i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1

                
        
        while theifs:
            x, y , thX , thY = theifs.popleft()
   
            for i, j in moves:
                if 0 <= x+i < n and 0 <= y+j < n and grid[x+i][y+j] == -1:
                    distance = abs(x+i-thX) + abs(y+j - thY)
                    grid[x+i][y+j] = distances[x+i][y+j] = distance
                    theifs.append((x+i, y+j, thX, thY))


        pq = [(-grid[0][0], 0, 0)]

        while pq:
            distance , x, y = heappop(pq)
            distance = -distance
            if (x == n-1 and y == n-1) or distance == 0:
                return distance
            grid[x][y] = -2
            for i, j in moves:
                    if 0 <= x+i < n and 0 <= y+j < n and grid[x+i][y+j] != -2:
                        d = min(distance, grid[x+i][y+j])
                        if distances[x+i][y+j] >= 0 or d < -distances[x+i][y+j]:
                            heappush(pq, (-d, x+i, y+j))
                            distances[x+i][y+j] = -d