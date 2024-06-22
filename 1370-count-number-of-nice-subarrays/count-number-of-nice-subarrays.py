class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        l = m = 0

        oddCount = 0
        result = 0

        for i in range(n):
            if nums[i]%2:
                oddCount += 1
            

            if oddCount > k:
                m += 1
                l = m
                oddCount -= 1

            if oddCount == k:
                while nums[m]%2 == 0:
                    m += 1
                result += (m-l+1)
            
        return result
                
    