class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        l,r = 1, max(quantities)


        while l <= r:
            m = (l+r)//2
            count = 0
            for q in quantities:
                count += math.ceil(q/m)

            if count > n:
                l = m + 1
            else:
                r = m -1
        
        return l
            