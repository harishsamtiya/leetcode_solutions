class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mydict = dict()
        mydict[0] = -1
        n = len(nums)
        count = 0
        result = 0
        for i in range(n):
            if nums[i]:
                count += 1
            else:
                count -= 1
            
            if count in mydict:
                result = max(result, i-mydict[count])
            else:
                mydict[count] =  i

        
        return result
        
            
            