class Solution:
    def frequencySort(self, s: str) -> str:
        
        chars_freq = [0]*75

        for ch in s:
            ind = ord(ch) - 48
            chars_freq[ind] += 1
        
        chars_freq = list(enumerate(chars_freq))
        chars_freq.sort(key=lambda x: x[1], reverse=True)

        st = ""
        for i in range(75):
            ind, freq = chars_freq[i]
            if freq == 0:
                break
            ch = chr(ind+48)
            st = st + ch*freq
        
        return st