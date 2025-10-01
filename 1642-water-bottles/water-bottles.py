class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0
        empty_bottles = 0

        while numBottles:
            result += numBottles
            total_bottles = numBottles + empty_bottles
            numBottles = total_bottles//numExchange
            empty_bottles = total_bottles%numExchange
        return result
        
