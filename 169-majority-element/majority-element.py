class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        element = nums[0]
        n = len(nums)
        for i in range(1, n):
            if count == 0:
                element = nums[i]
                count = 1
            else:
                if element == nums[i]:
                    count += 1
                else:
                    count -= 1
        return element