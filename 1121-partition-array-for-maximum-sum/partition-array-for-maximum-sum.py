class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        dp = [-1]*n

        def fun(ind):
            if ind >= n:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            maxi = 0
            ans = 0
            for j in range(ind, min(ind + k, n)):
                maxi = max(maxi, arr[j])
                ans = max(maxi*(j+1-ind) + fun(j+1),ans)
            
            dp[ind] = ans
            return ans

        return fun(0)