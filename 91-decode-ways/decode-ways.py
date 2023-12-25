class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [0]*(n+1)
        memo[n] = 1
        if s[n-1] == '0':
            memo[n-1] = 0
        else:
            memo[n-1] = 1

        
        for i in range(n-2, -1, -1):
            if s[i] == '0':
                memo[i] = 0
            else:
                count = memo[i+1]

                if eval(s[i:i+2]) < 27:
                    count += memo[i+2]
                
                memo[i] = count
        
        return memo[0]
            
        
