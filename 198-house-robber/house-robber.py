class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        prev = prev_prev = 0

        for i in range(n):
            prev_prev, prev = prev, max(prev_prev + nums[i], prev)

        return prev