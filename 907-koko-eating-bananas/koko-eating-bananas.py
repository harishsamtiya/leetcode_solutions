class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, 0
        n = len(piles)

        if n > h:
            return -1

        for pile in piles:
            r = max(r, pile)
            l += pile
        l = max(l//h, 1)

        def cal_time(k):
            try_h = 0
            for pile in piles:
                try_h += ceil(pile/k)

            return try_h

        ans = r
        while l <= r:
            mid = (l+r)//2
            try_h = cal_time(mid)

            if try_h > h:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1

        return ans
