class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 1000000007

        dp = [0]*(k+1)
        dp[0] = 1

        for i in range(1, n+1):
            temp = [0]*(k+1)
            total = 0
            for j in range(0, k+1):
                if j >= i:
                    total -= dp[j-i]
                total += dp[j]
                total %= MOD
                temp[j] = total
            dp = temp
        return dp[k]