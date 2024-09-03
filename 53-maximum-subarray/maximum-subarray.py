class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        summ = nums[0]
        maxSum = nums[0]
        
        for num in nums[1:]:
            if summ < 0:
                summ = num
            else:
                summ += num
            
            maxSum = max(summ, maxSum)

        return maxSum