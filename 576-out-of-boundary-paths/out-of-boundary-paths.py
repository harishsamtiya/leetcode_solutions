class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        cache = {}
        mod = 10**9 + 7
        def dfs(row, col, moves):
            if (row < 0 or col < 0) or (row == m or col == n):
                return 1
            if moves == 0:
                return 0
            if (row, col, moves) in cache:
                return cache[(row, col, moves)]
            ans = ((dfs(row -1, col, moves-1) +
            dfs(row+1, col, moves-1))%mod+
            (dfs(row, col-1, moves-1)+
            dfs(row, col+1, moves-1))%mod)%mod
            
            cache[(row, col, moves)] = ans

            return ans

        
        return dfs(startRow, startColumn, maxMove)
