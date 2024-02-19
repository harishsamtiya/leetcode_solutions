class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        n = abs(n)
        powers = [1]*32
        for i in range(1, 32):
            powers[i] = 2*powers[i-1]

        l, r = 0, 31

        while l <= r:
            mid = (l+r)//2

            if powers[mid] == n:
                return True
            elif powers[mid] > n:
                r = mid -1
            else:
                l = mid + 1
        return False
            
            