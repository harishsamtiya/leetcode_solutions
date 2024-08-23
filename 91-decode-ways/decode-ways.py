class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        a1, a2 = 1, 1
        if s[-1] == '0':
            a1 = 0
        
        for i in range(n-2, -1,-1):
            curr = 0
            if s[i] != '0':
                curr = a1
                if 0 < int(s[i: i+2]) < 27:
                    curr += a2
            a1, a2 = curr, a1
        
        return a1
                
        

            
