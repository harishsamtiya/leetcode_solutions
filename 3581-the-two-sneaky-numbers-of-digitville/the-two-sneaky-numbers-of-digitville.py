class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    result.append(nums[i])
        
        return result