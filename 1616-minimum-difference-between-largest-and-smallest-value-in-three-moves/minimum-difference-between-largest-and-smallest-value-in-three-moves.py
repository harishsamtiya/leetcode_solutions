class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 5:
            return 0
        
        mins = []
        heapify(nums)
        for i in range(4):
            mins.append(heappop(nums))
        
        maxs = []
        nums = [-num for num in nums]
        heapify(nums)
        m = len(nums)
    
        for i in range(min(4, m)):
            maxs.append(-heappop(nums))
        
        if m < 4:
            for i in range(4-m):
                maxs.append(mins[-1-i])
        
        ans = maxs[0] - mins[0]
        for i in range(4):
            ans = min(ans, maxs[-1-i] - mins[i])

        return ans