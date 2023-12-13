class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        rows = [0]*n
        cols = [0]*m
        count = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j]:
                    rows[i] += 1
        
        for j in range(m):
            for i in range(n):
                if mat[i][j]:
                    cols[j] += 1
        
        for i in range(n):
            if rows[i] == 1:
                for j in range(m):
                    if cols[j] == 1 and mat[i][j]:
                        count += 1
        return count