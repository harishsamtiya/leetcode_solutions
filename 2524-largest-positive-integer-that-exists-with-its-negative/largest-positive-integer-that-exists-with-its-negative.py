class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        ans = -1
        myset = set()

        for num in nums:
            if -num in myset:
                ans = max(ans, abs(num))
            myset.add(num)
        return ans