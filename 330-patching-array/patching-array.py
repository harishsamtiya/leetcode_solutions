class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        ind, start, end = 0, 0, 0
        m = len(nums)
        count = 0

        while end < n:
            
            if ind < m and end + 1 >= nums[ind]:
                end += nums[ind]
                ind += 1
            else:
                count += 1
                end += end + 1
        return count