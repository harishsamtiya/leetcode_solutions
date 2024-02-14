class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos, neg = [], []

        for i in range(n):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        for i in range(0, n, 2):
            nums[i] = pos.pop(0)
            nums[i+1]= neg.pop(0)
        return nums
        