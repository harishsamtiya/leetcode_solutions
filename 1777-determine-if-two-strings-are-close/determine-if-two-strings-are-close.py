class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n = len(word1)

        if n != len(word2):
            return False
                
        chars1 = [0]*26
        chars2 = [0]*26

        for i in range(n):
            chars1[ord(word1[i])-97] += 1
            chars2[ord(word2[i])-97] += 1

        for i in range(26):
            if (chars1[i] == 0 and chars2[i] != 0 )or (chars2[i] ==0 and chars1[i]!=0):
                return False
        
        chars1.sort()
        chars2.sort()
        return chars1 == chars2

