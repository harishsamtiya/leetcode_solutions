class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        lis = [1]*n
        ans = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1+ lis[j])
            ans= max(lis[i], ans)
        return ans
            