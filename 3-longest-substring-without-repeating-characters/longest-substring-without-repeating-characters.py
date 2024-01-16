class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mydict = dict()
        n = len(s)
        if n == 0:
            return 0

        ans = 0
        l = 0
        for i in range(n):
            if s[i] in mydict:
                l = max(mydict[s[i]] + 1, l ) 
            mydict[s[i]] = i
            ans = max(ans, i-l+1)

        return ans