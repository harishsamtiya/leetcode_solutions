class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        n = len(s)
        prev = ' '
        for ch in s:
            if prev == ' ':
                if ch != ' ':
                    count = 1
            elif ch != ' ':
                count += 1
        
            prev = ch
        return count
            