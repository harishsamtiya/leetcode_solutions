class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] 
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        l, r = 0, n-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == nums[mid-1]:
                if (r-mid)%2:
                    l = mid+1 
                else:
                    r = mid -2
            elif nums[mid] == nums[mid+1]:
                if (r-mid-1)%2:
                    l = mid+2
                else:
                    r = mid -1
            else:
                return nums[mid]
        return -1
