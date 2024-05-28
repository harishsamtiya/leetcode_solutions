class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)

        i, j = 0, 0
        result = 0
        while j < n:


            val = abs(ord(s[j]) - ord(t[j]))
            if val <= maxCost:
                maxCost -= val
                j += 1
            else:
                result = max(result, j-i)

                while maxCost < val and i < j:
                    q = abs(ord(s[i])-ord(t[i]))
                    maxCost += q
                    i += 1
                
                if maxCost < val:
                    i += 1
                    j += 1
            
        
        result = max(result, j-i)
        return result