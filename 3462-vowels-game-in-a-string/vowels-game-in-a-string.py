class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = 0

        for ch in s:
            if ch in ('a', 'i', 'o', 'u', 'e'):
                count += 1
        
        if count%2:
            return True
        else:
            if count == 0:
                return False
            return True

