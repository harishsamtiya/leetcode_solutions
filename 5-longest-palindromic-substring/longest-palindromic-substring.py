class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s[0]
        elif n == 2:
            if s[0]  == s[1]:
                return s
            else:
                return s[0]
        longest = 0
        st = ""

        for i in range(1, n):

            p, q = i, i
            while p >= 0 and q < n:
                if s[p] != s[q]:
                    break
                p -= 1
                q += 1

            p += 1
            q -= 1
            if q - p + 1 > longest:
                longest = q - p + 1
                st = s[p: q+1]

            
            p, q = i-1, i
            while p >= 0 and q < n:
                if s[p] != s[q]:
                    break
                p -= 1
                q += 1

            p += 1
            q -= 1
            if q - p + 1 > longest:
                longest = q - p + 1
                st = s[p: q+1]

        
        return st
            
