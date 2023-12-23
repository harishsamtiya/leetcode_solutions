class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        myset = set(nums)
        visited = set()
        maxi = 0
        for i in range(n):
            if nums[i] not in visited:
                count = 1
                curr = nums[i] - 1
                while curr in myset:
                    visited.add(curr)
                    curr -= 1
                    count += 1
                
                curr = nums[i] + 1
                while curr in myset:
                    visited.add(curr)
                    curr += 1
                    count += 1

                maxi =max(maxi, count)
        return maxi