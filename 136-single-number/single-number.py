class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        num = 0

        for val in nums:
            num ^= val

        return num