class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        myset = set()
        for a in range(0, int(c**(0.5))+1):
            a2 = a*a
            myset.add(a2)
            b2 = c - a2

            if b2 in myset:
                return True
        
        return False