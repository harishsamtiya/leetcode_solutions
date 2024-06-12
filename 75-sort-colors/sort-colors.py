class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zeroCount = 0
        oneCount = 0

        for num in nums:
            if num == 0:
                zeroCount += 1
            elif num == 1:
                oneCount += 1
        
        n = len(nums)
        i = 0
        while zeroCount > 0:
            nums[i] = 0
            zeroCount -= 1
            i += 1
        
        while oneCount > 0:
            nums[i] = 1
            oneCount -= 1
            i += 1
        
        while i < n:
            nums[i] = 2
            i += 1
