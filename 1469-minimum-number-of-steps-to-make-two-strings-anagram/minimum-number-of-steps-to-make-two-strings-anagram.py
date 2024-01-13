class Solution:
    def minSteps(self, s: str, t: str) -> int:
        chars = [0]*26

        for ch in s:
            chars[ord(ch) - 97] += 1
        
        for ch in t:
            chars[ord(ch) - 97] -= 1
        
        summ = 0
        for num in chars:
            if num > 0:
                summ += num
        return summ