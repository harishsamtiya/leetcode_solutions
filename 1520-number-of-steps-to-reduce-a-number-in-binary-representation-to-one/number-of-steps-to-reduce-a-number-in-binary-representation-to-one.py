class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        s = [int(ch) for ch in s]

        result = 0
        for i in range(n-1, -1, -1):
            if i == 0 and s[0] == 1:
                break
            if s[i] == 1:
                for j in range(i-1, -1, -1):
                    if s[j] == 0:
                        s[j] = 1
                        break
                    else:
                        s[j] = 0

                result += 1
            result += 1
        

        return result
