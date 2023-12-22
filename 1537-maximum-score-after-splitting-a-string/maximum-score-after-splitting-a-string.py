class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        total_ones = 0
        for ch in s:
            if ch == '1':
                total_ones += 1

        zeros = 0
        maxi = 0
        for i in range(n-1):
            if s[i] == '0':
                zeros += 1
            
            maxi = max(maxi, zeros + total_ones - (i+1 - zeros))

        return maxi




