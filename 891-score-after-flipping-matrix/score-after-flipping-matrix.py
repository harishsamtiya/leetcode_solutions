class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] =  0 if grid[i][j] == 1 else 1
        
        for j in range(m):
            count = 0
            for i in range(n):
                if grid[i][j] == 1:
                    count += 1
            
            if count < (n+1)//2:
                for i in range(n):
                    grid[i][j] = 0 if grid[i][j] == 1 else 1

        
        result = 0
        print(grid)
        for i in range(n):
            num = 0
            for j in range(m):
                if grid[i][j]:
                    num += 2**(m-j-1)
            print(num)
            result += num

        return result