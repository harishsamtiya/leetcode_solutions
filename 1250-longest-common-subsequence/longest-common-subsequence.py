class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        memo = [0]*(m+1)

        for i in range(n-1, -1, -1):
            temp = [0]*(m+1)
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    temp[j] = memo[j+1] +1 
                else:
                    temp[j] = max(temp[j+1], memo[j])
            memo = temp
        return memo[0]