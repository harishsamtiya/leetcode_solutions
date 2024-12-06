class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        count = 0
        summ = 0

        for num in range(1, n+1):
            if num not in banned:
                summ += num
                if summ > maxSum:
                    break
                count += 1

        return count