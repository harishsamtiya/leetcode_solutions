class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(n):
            distinct_count = [0]*26
            chr_count = 0
            max_freq = 0
            chr_max_count = 0

            for j in range(i, n):
                ind = ord(s[j]) - ord('a')
                distinct_count[ind] += 1

                if distinct_count[ind] == 1:
                    chr_count += 1

                if distinct_count[ind] == max_freq:
                    chr_max_count += 1

                if distinct_count[ind] > max_freq:
                    max_freq = distinct_count[ind]
                    chr_max_count = 1
                
                if chr_max_count == chr_count:
                    result = max(result, j-i+1)
        return result

