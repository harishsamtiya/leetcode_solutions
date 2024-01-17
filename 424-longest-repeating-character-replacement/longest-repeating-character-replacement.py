class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        array = [0]*26

        maxf = 0
        l = 0
        result = 0
        n = len(s)
        for r in range(n):
            array[ord(s[r]) - 65] += 1
            maxf = max(maxf, array[ord(s[r]) - 65])
            while (r-l+1) - maxf > k:
                array[ord(s[l]) - 65] -= 1
                l += 1
            result = max(result, r-l+1)
        return result