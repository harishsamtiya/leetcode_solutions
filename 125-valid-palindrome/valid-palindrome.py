class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []

        for ch in s:
            asci = ord(ch)
            print(asci, ch)
            if 65 <= asci <= 90:
                asci += 32
                ch = chr(asci)

            if 48 <= asci <= 57 or 97 <= asci <= 122:
                l.append(ch)

        n = len(l)
        for i in range(n//2):
            if l[i] != l[n-1-i]:
                return False

        return True