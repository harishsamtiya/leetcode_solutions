class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        l,r = 0, n-1

        while l<r:
            if s[l] != s[r]:
                break

            while l < r and s[l+1] == s[l]:
                l +=1

            while r > l and s[r-1] == s[r]:
                r -= 1
            
            l+=1
            r-=1
        return r-l+1 if r >= l else 0