class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # if k == 0:
        #     return 0
        pro = 1
        result = 0

        i, j = 0, 0

        while j < n:
            if nums[j] < k:
                result += 1
                pro = pro*nums[j]
                while pro >= k:
                    pro = pro//nums[i]
                    i += 1
                result += j-i
                j += 1
            else:
                j += 1
                i = j
                pro = 1

        return result

