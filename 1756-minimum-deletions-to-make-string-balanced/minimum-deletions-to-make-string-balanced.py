class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        aTotal = 0
        bTotal = 0

        for ch in  s:
            if ch == 'a':
                aTotal += 1
            else:
                bTotal += 1

        aCount = 0
        bCount = 0
        result = min(aTotal, bTotal)
        for ch in s:
            if ch == 'a':  
                aCount += 1
            else:
                bCount += 1

            result = min(result, bCount + aTotal - aCount)
        
        return result
