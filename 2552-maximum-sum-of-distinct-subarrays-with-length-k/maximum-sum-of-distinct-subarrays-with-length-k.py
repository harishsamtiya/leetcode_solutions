class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        summ = 0
        result = 0
        mydict = dict()

        for r in range(n):
            summ += nums[r]

            if nums[r] in mydict:
                temp = mydict[nums[r]] + 1
                for i in range(l, temp):
                    summ -= nums[i]
                    del mydict[nums[i]]
                l = temp
            
            mydict[nums[r]] = r  
            if r-l+1 == k:
                result = max(result, summ)
                summ -= nums[l]

                del mydict[nums[l]]
                l += 1

            
        return result