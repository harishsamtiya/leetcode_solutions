class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        result = 0

        prev_summ = 0

        for i in range(n):
            if nums[i] == 0:
                diff = abs(prev_summ - (total - prev_summ - nums[i]))
                if diff == 0:
                    result += 2
                elif diff == 1:
                    result += 1

            prev_summ += nums[i]  
        return result              