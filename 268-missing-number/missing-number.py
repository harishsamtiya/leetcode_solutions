class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nsumm = n*(n+1)//2
        return nsumm - sum(nums)