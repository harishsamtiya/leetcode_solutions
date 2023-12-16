class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0]*26

        for ch in s:
            index = ord(ch) - 97
            letters[index] += 1
        

        for ch in t:
            index = ord(ch) - 97
            letters[index] -= 1

        for i in range(26):
            if letters[i] != 0:
                return False

        return True