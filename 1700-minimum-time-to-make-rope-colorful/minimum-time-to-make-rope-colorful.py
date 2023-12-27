class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(neededTime)

        i = 1
        prev = colors[0]
        result = 0
        while i < n:
            if prev == colors[i]:
                summ = 0
                maxi = 0

                j = i-1
                while j < n and prev == colors[j]:
                    summ += neededTime[j]
                    maxi = max(maxi, neededTime[j])
                    j += 1
                i = j
                result += (summ - maxi)
            if i < n:
                prev = colors[i]
            i += 1
        
        return result
            
