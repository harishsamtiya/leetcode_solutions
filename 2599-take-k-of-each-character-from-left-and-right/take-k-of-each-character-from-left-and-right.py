class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        count = {'a': 0, 'b': 0, 'c':0}

        for ch in s:
            count[ch] += 1  

        def condition(count):
            for val in count.values():
                if val < k:
                    return False
            return True
        
        if not condition(count):
            return -1

        l = 0
        maxi = 0
        for r in range(n):
            count[s[r]] -= 1

            if condition(count):
                maxi = max(maxi, r-l+1)
            else:
                while l < r and not condition(count):
                    count[s[l]] += 1
                    l += 1
                if condition(count):
                    maxi = max(maxi, r-l+1)
            
        return n - maxi