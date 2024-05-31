class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for num in nums:
            xor ^= num
        
        shift = 0
        while shift < 32:
            if (xor & 1) == 1:
                break
            xor = xor >> 1
            shift += 1

        xor0 = 0
        xor1 = 0

        for num in nums:
            temp = num >> shift
            if (temp & 1) == 0:
                xor0 ^= num
            else:
                xor1 ^= num
        
        return [xor0, xor1]