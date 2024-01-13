class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        n = len(prices)
        maxi = 0
        for i in range(n):
            if prices[i] <= buy:
                buy = prices[i]
            else:
                maxi = max(maxi ,prices[i] - buy)
        return maxi
