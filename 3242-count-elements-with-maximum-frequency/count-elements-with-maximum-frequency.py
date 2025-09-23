class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        numCount = dict()

        for num in nums:
            if num in numCount:
                numCount[num] += 1
            else:
                numCount[num] = 1
        
        maxFreq = 0
        result = 0
        for freq in numCount.values():

            if maxFreq < freq:
                maxFreq = freq
                result = 0
            if maxFreq == freq:
                result += freq
        return result