class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s)
        a_count = 0
        b_count = 0
        for i in range(n//2):
            if s[i] in vowel:
                a_count += 1
        for i in range(n//2, n):
            if s[i] in vowel:
                b_count += 1
        
        if a_count == b_count:
            return True
        return False