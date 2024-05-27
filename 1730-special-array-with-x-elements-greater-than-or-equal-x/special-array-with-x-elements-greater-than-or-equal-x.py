class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        if n <= nums[0]:
            return n

        for i in range(1, n):
            x = n-i
            if nums[i-1] < x <= nums[i]:
                return x
        return -1

