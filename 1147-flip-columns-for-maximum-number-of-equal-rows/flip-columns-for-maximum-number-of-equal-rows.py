class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        counts = [0]*m

        def func(i, j):
            
            flag = True
            for k in range(n):
                if matrix[i][k] != matrix[j][k]:
                    flag = False
                    break
            if flag:
                return True    
            
            for k in range(n):
                if matrix[i][k] == matrix[j][k]:
                    return False
            
            return True
            
        for i in range(m):
            c = 1
            for j in range(i+1, m):

                if func(i, j):
                    c += 1
            counts[i] = c
        
        return max(counts)
        
