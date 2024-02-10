class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        cache = [None]*n

        def fun(i):
            if cache[i] :
                return cache[i]
            res = [nums[i]]  

            for j in range(i+1, n):
                if nums[j] % nums[i] == 0:

                    temp = [nums[i]] + fun(j)

                    if len(temp) > len(res):
                         res = temp
            cache[i] = res
            return res


        res = []
        for i in range(n):
            tmp = fun(i)
            if len(tmp) > len(res):
                res = tmp
        
        return res


