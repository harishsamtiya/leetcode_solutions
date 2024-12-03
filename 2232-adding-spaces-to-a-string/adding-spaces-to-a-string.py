class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.sort()
        j = 0
        n = len(spaces)
        result = ""
        c = 0

        for i in range(len(s)):
            ch = s[i]
            if j < n and i == spaces[j]:
                result += " "
                j += 1

            result += ch
        
        return result