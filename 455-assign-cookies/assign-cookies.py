class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        m = len(g)
        n = len(s)
        ind = 0
        count = 0
        for i in range(n):
            if g[ind] <= s[i]:
                ind += 1
                count += 1
                if ind == m:
                    break
        return count
            
            