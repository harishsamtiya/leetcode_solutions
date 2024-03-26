class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            num = nums[i]
            if 0 < num <= n and num != nums[num-1]:
                nums[i] = nums[num-1]
                nums[num-1] = num
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i+1:
                return i+1

        return n+1