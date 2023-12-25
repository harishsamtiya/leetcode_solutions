class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev_prev = 1
        if s[n-1] == '0':
            prev = 0
        else:
            prev = 1

        
        for i in range(n-2, -1, -1):
            if s[i] == '0':
                curr = 0
            else:
                count = prev

                if eval(s[i:i+2]) < 27:
                    count += prev_prev
                
                curr = count
            prev_prev = prev
            prev = curr
        
        return prev
            
        
