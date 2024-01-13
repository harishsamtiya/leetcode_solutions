class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        ans = 2 
        if a == e:
            if c == a and (b < d < f or b > d > f):
                pass
            else:
                return 1
        
        if b == f:
            if b == d and (a < c < e or a > c > e):
                pass
            else:
                return 1
        
        if c + d == e + f :
            if c + d == a + b and (c < a < e  or c > a > e):
                pass
            else:
                return 1
        
        if c-d == e - f:
            if  c-d == a - b and (c < a < e  or c > a > e):
                pass
            else:
                return 1
        return 2
