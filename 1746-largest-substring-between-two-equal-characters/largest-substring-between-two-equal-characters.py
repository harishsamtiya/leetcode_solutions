class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        li = [[301, -1] for _ in range(26)]
        n = len(s)
        for i in range(n):
            ind = ord(s[i]) - 97
            li[ind][0] = min(li[ind][0], i)
            li[ind][1] = max(li[ind][1], i)
        

        ans = -1
        for x, y in li:
            leng = y-x-1
            if leng >= 0 and leng > ans:
                ans = leng
        return ans