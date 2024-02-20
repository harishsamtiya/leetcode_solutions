class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        leftsum = 0
        summ = sum(nums)

        for i in range(n):
            rightsum = summ - nums[i] - leftsum
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1
