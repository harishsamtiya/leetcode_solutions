class Solution:
    def findMin(self, nums: List[int]):
        n = len(nums)
        l , r = 0, n-1

        if nums[l] <= nums[r]:
            return nums[0]

        while l < r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]