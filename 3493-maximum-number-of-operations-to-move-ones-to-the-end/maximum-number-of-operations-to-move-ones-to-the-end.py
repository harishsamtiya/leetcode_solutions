class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        onesCount = 0
        opr = 0

        for i in range(n):
            if s[i] == '1':
                onesCount += 1
            elif i+1 == n or s[i+1] == '1':
                opr += onesCount
      
        return opr
