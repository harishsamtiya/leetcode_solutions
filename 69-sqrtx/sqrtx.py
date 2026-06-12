class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        l, r = 0, ceil(x/2)

        while l <= r:
            m = (r + l)//2
            sq = m*m
            if sq > x:
                r = m -1
            else:
                l = m + 1

        print(l)
        return l -1