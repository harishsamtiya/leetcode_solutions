class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        pro = 1
        prev = 1
        for i in range(n):
            pro *= prev
            ans.append(pro)
            prev = nums[i]

        pro = 1
        prev = 1
        for i in range(n-1, -1, -1):
            pro *= prev
            ans[i] *= pro
            prev = nums[i]

        return ans
