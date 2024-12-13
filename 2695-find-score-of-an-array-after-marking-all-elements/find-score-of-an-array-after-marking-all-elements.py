class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        n = len(nums)
        temp = [(num, i) for i, num in enumerate(nums)]
        heapify(temp)

        while temp:
            num, ind = heappop(temp)
            
            if nums[ind] > 0:
                nums[ind] = -num
                score += num

                if ind -1 >= 0 and nums[ind-1] > 0:
                    nums[ind-1] = -nums[ind-1]
                
                if ind+1 < n and nums[ind+1] > 0:
                    nums[ind+1] = -nums[ind+1]
 
        return score