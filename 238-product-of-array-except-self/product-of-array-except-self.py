class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        foundZero = 0
        for num in nums:
            if num == 0:
                foundZero += 1
            else:
                prod *= num
        if foundZero > 1:
            return [0]*n
        result = []
        for num in nums:
            if num != 0:
                if foundZero:
                    result.append(0)
                else:
                    result.append(prod//num)
            else:
                result.append(prod)
        return result
