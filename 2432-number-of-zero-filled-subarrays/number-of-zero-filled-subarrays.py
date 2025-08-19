class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        sub_zero_count = 0
        
        for num in nums:
            if num == 0:
                sub_zero_count += 1
            else:
                sub_zero_count = 0
            result += sub_zero_count
        return result