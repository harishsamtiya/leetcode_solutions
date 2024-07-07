class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles

        while numBottles >= numExchange:
            q = numBottles//numExchange
            r = numBottles -q*numExchange
            count += q
            numBottles = q + r
        
        return count