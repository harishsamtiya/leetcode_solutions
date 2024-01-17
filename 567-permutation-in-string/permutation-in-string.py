class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        array = [[0, 0] for _ in range(26)]
        n = len(s1)

        for ch in s1:
            ind = ord(ch)-97
            array[ind][0] += 1
        
        l = 0
        n2 = len(s2)
        for r in range(n2):
            ind = ord(s2[r])-97
            array[ind][1] += 1

            while array[ind][1] > array[ind][0]:
                array[ord(s2[l])-97][1] -= 1
                l += 1
            
            if (r-l+1) == n:
                return True
        return False




