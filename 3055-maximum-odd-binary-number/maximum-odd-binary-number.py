class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        oneCount = 0

        for ch in s:
            if ch == '1':
                oneCount += 1

        return "1"*(oneCount-1) + "0"*(n-oneCount) + "1"*(1)

