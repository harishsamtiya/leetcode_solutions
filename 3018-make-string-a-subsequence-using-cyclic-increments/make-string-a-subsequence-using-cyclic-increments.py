class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n, m = len(str1), len(str2)

        i, j = 0, 0

        while i < n and j < m:
            ch2 = str2[j]
            ch1 = str1[i]
            asci = ord(ch1) + 1
            asci = 97 if asci == 123 else asci


            if ch1 == ch2 or ch2 == chr(asci):
                j += 1
            i += 1
        
        if j >= m:
            return True
        
        return False