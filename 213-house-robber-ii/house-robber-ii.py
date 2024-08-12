class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def solve(start, end):
            a1, a2 = 0, 0

            for i in range(start, end):
                a2, a1 = max(a2, a1 + nums[i]), a2
            return max(a1, a2)
        
        return max(solve(0, n-1), solve(1, n))