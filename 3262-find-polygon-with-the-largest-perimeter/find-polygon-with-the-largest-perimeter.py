class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        print(nums)
        summ = sum(nums)

        for num in nums:
            summ -= num
            if num < summ:
                return num + summ
        
        return -1