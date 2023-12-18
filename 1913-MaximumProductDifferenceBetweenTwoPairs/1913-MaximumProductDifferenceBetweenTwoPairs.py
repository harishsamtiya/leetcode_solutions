class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        maxi = smaxi = 0
        mini = smini = 10**4 + 1
        n = len(nums)
        for num in nums:
            temp = num
            if num > maxi:
                maxi, num = num, maxi
            
            if num > smaxi:
                smaxi = num

            if mini > temp:
                mini, temp = temp, mini

            if smini > temp:
                smini = temp

        return maxi*smaxi - mini*smini
