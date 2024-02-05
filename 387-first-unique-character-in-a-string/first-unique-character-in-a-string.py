class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        chars = [n]*26

        for i in range(n):
            ind = ord(s[i]) - 97
            if chars[ind] == n:
                chars[ind] = i
            else:
                chars[ind] = n + 1 
        
        ans = n 
        for fre in chars:
            ans = min(fre, ans)
        
        return -1 if ans == n else ans