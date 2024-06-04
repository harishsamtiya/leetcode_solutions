class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCount = [0]*58
        
        for ch in s:
            ind = ord(ch) - 65
            charCount[ind] += 1

        oddCounted = False
        result = 0
        for num in charCount:
            count = (num//2)*2
            result += count

            if not oddCounted and num > count:
                result += 1
                oddCounted = True

        return result