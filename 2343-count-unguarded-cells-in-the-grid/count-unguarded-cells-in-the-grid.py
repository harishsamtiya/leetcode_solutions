class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        array = [[0]*n for _ in range(m)]

        for i, j in walls:
            array[i][j] = 2

        for i, j in guards:
            array[i][j] = 1
        
        def func(i, j):
            nonlocal isGuard

            if array[i][j] == 1:
                isGuard = True
            elif array[i][j] == 2:
                isGuard = False
            elif isGuard:
                array[i][j] = 3

        for j in range(n):
            isGuard = False
            for i in range(m):
                func(i, j)

            isGuard = False
            for i in range(m-1, -1, -1):
                func(i, j)
        
        for i in range(m):
            isGuard = False
            for j in range(n):
                func(i, j)

            isGuard = False
            for j in range(n-1, -1, -1):
                func(i, j)
        
        count = 0

        for i in range(m):
            for j in range(n):
                if array[i][j] == 0:
                    count += 1
        
        return count

