class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        array = [-1]*100
        def solve(i):
            if i >= n:
                return 1
            elif s[i] == '0':
                return 0
            elif array[i] != -1:
                return array[i]
            
            temp = solve(i+1)

            if i+1 < n and 0 < int(s[i: i+2]) < 27:
                temp += solve(i+2)

            array[i] = temp
            return temp
        
        return solve(0)
        

            
