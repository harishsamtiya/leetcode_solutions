class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mini = 101
        smini = 101

        for price in prices:
            if price < mini:
                mini, price = price, mini
            
            if price < smini:
                smini = price

        
        return money - (mini + smini) if money - (mini + smini) >= 0 else money
            
