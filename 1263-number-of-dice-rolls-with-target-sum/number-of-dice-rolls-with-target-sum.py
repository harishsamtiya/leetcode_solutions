class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = dict()
        def fun(n, total):
            if n == 0 :
                return 1 if total == 0 else 0
            elif (n, total) in dp:
                return dp[(n, total)]
            elif n < 0:
                return 0
            count = 0
            for i in range(1, k+1):
                count += fun(n-1, total - i)
            ans = count%mod
            dp[(n, total)] = ans
            return ans
        
        return fun(n, target)

