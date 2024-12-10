class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)

        def is_possible(win_size):
            p, q = 0, 0
            arr = [0]*26

            for q in range(n):
                while win_size < q - p +1:
                    p += 1
                
                if s[p] != s[q]:
                    p = q
                
                if q - p + 1 == win_size:
                    arr[ord(s[p])-ord('a')] += 1
                    if arr[ord(s[p])-ord('a')] == 3:
                        return True
            return False


        l, r = 1, n-1
        ans = -1

        while l <= r:
            mid = (l+r)//2

            if is_possible(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans

