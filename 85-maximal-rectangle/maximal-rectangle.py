class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        memo = [0]*m
        
        def maxAreaofHisto(memo):
            stack = []
            maxArea = 0

            for i in range(m):
                if not stack or memo[i] > stack[-1][1]:
                    stack.append((i, memo[i]))
                else:
                    ind = i
                    while stack and memo[i] < stack[-1][1]:
                        ind, val = stack.pop()
                        maxArea = max(maxArea, (i-ind)*val)
                    
                    if not stack or stack[-1][1] < memo[i]:
                        stack.append((ind, memo[i]))

                    
            while stack:
                ind, val = stack.pop()
                maxArea = max(maxArea, (m-ind)*val)
            return maxArea
        
        result = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    memo[j] = 0
                else:
                    memo[j] += 1
            print(memo)
            result = max(result,maxAreaofHisto(memo))
        return result