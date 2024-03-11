class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ch_count = [0]*26

        for ch in s:
            ind = ord(ch) - 97
            ch_count[ind] += 1
        
        resultStr = ""

        for ch in order:
            ind = ord(ch) - 97
            if ch_count[ind]:
                resultStr += chr(ind+97)*ch_count[ind]
                ch_count[ind] = 0
        
        for ind in range(26):
            if ch_count[ind]:
                resultStr += chr(ind+97)*ch_count[ind]
        
        return resultStr