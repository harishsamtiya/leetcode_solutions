class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = n 

        cache = [[True]*n]
        temp = []

        for i in range(n-1):
            if s[i] == s[i+1]:
                temp.append(True)
                ans += 1
            else:
                temp.append(False)
        
        cache.append(temp)
        for j in range(3, n+1):
            temp = []
            for i in range(n-j+1):
                if s[i] == s[i+j-1] and cache[0][i+1]:
                    temp.append(True)
                    ans += 1
                else:
                    temp.append(False)
            cache.pop(0)
            cache.append(temp)
        return ans