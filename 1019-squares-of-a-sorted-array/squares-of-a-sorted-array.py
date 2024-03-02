class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        ind = -1
        n = len(nums)
        for i in range(n):
            if nums[i] >= 0:
                ind = i
                break
        
        if ind == -1:
            i, j = n-1, n
        else:
            i, j = ind -1, ind

        while 0 <= i and j < n:
            if abs(nums[i]) <= abs(nums[j]):
                result.append(nums[i]*nums[i])
                i -= 1
            else:
                result.append(nums[j]*nums[j])
                j += 1

        while 0 <= i:
            result.append(nums[i]*nums[i])
            i -= 1

        while j < n:
            result.append(nums[j]*nums[j])
            j += 1
        return result