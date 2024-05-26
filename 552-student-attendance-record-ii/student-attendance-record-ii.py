class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3
        
        mod = 1000000007

        memo = [[1, 1, 0], [1, 0, 0]]

        for i in range(2, n+1):
            tmp = [[0, 0, 0], [0, 0, 0]]

            tmp[0][0] += (((memo[0][0] + memo[0][1])%mod) + memo[0][2])%mod
            tmp[1][0] += (((memo[1][0] + memo[1][1])%mod) + memo[1][2])%mod

            tmp[1][0] = (tmp[1][0] + tmp[0][0])%mod

            tmp[0][1] = memo[0][0]
            tmp[1][1] = memo[1][0]
            tmp[0][2] = memo[0][1]
            tmp[1][2] = memo[1][1]

            memo = tmp
        

        summ = 0
        for arr in memo:
            for num in arr:
                summ = (summ + num)%mod
        return summ
