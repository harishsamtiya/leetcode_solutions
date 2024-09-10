class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        array = [10001]*n
        array[0] = 0
        ind = 0
        for i in range(n-1):
            jumps = nums[i]

            for j in range(ind+1, min(i+jumps+1, n)):
                array[j] = min(array[j], array[i]+1)

            ind = max(ind, i + jumps)
        return array[n-1]