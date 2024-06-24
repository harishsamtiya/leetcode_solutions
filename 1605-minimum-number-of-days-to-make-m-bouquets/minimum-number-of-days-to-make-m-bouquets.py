class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if m*k > n:
            return -1

        def canPossible(tillday):
            bouquetsMade = 0
            flowersCollected = 0


            for day in bloomDay:
                if day <= tillday:
                    flowersCollected += 1
                    if flowersCollected == k:
                        bouquetsMade += 1
                        flowersCollected = 0
                else:
                    flowersCollected = 0
            
            return bouquetsMade >= m

        l = min(bloomDay)
        r = max(bloomDay)

        ans = -1
        while l <= r:
            mid = (l+r)//2 

            if canPossible(mid):
                ans = mid 
                r = mid -1
            else:
                l = mid + 1
        
        return ans