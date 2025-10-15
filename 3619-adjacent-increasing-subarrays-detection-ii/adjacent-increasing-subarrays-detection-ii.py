class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        prevInc = 0
        currInc = 1
        prevNum = nums[0]
        for i in range(1, n):
            if nums[i] > prevNum:
                currInc += 1
            else:
                ans = max(min(prevInc, currInc), ans)
                prevInc = currInc 
                currInc = 1
            ans = max(min(currInc//2, currInc -currInc//2), ans)
            prevNum = nums[i]

        ans = max(min(prevInc, currInc), ans)
        return ans