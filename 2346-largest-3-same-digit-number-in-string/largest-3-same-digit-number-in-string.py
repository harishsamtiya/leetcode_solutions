class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        result = ''
        max_int = -1

        for i in range(n-2):
            if num[i] == num[i+1] == num[i+2] and int(num[i]) > max_int:
                result = num[i: i+3]
                max_int = int(num[i])
        return result