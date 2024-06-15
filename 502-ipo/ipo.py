class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapify(minCapital)
        
        for l in range(k):
            while minCapital and minCapital[0][0] <= w:
                c,p = heappop(minCapital)
                heappush(maxProfit, -p)

            if not maxProfit: 
                break
        
            w += -1*heappop(maxProfit)
        
        return w
