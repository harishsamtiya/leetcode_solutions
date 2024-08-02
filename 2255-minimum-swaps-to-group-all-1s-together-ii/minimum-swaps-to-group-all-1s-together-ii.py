class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        totalOne = 0

        for num in nums:
            if num:
                totalOne += 1
        
        l = 0
        gap = 0
        result = totalOne
        for r in range(n + totalOne-1):
            tempR = r%n
            if nums[tempR] == 0:
                gap += 1
            
            if (r - l+ 1) > totalOne:
                if nums[l] == 0:
                    gap -= 1
                l += 1
            
            if (r - l+ 1) == totalOne:
                result = min(result, gap)

        
        return result