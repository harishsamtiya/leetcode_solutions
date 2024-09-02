class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        summ = sum(chalk)
        k = k%summ

        for i in range(n):
            if chalk[i] > k:
                return  i
            k -= chalk[i]
        return -1