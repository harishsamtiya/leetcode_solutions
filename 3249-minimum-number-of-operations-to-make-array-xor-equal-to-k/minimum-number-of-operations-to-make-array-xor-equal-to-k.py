class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        result = 0
        while k > 0 or xor > 0:
            if k & 1 != xor & 1:
                result += 1
            k  = k >> 1
            xor = xor >> 1

        return result