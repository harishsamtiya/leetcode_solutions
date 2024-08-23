class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        memo = dict()
        def solve(amount):
            if amount == 0:
                return 0
            elif amount in memo:
                return memo[amount]
            ans = 100000
            for coin in coins:
                if coin > amount:
                    break
                ans = min(solve(amount - coin), ans)
            memo[amount] = ans + 1
            return ans + 1
        
        result = solve(amount)
        if result > amount:
            return -1
        return result
            
            

