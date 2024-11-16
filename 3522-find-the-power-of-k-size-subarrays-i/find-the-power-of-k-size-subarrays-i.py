class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        temp = 0
        result = []
        for i in range(1, k):
            if nums[i-1] + 1 != nums[i]:
                temp = i
        
        l = temp
        

        for r in range(k-1, n):

            if l == r or (nums[r-1] + 1 == nums[r]):
                if (r - l + 1) == k :
                    result.append(nums[r])
                    l += 1
                else:
                    result.append(-1)
            else:
                l = r
                result.append(-1)
        
        return result