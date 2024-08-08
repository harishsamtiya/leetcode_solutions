class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        result = []
        steps = 1

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        count = 0
        i = 0

        while rows*cols > count:
            for p in range(2):
                dr, dc = dirs[i]
                for q in range(steps):
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        result.append([rStart, cStart])
                        count += 1
                    rStart, cStart = rStart + dr, cStart + dc
                    
                i = (i +1)%4
            steps += 1
        return result
