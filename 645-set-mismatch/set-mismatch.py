class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        true_sum = n*(1 + n)//2
        summ = sum(nums)
        myset = set()
        double = -1
        for num in nums:
            if num in myset:
                double = num
                break
            myset.add(num)
        summ -= double

        return [num, true_sum - summ]